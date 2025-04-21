import re
from tabulate import tabulate


class SymbolTable:
    def __init__(self):
        self.symbols = []

    def add_variable(self, name, dtype, value):
        self.symbols.append(
            {
                "Name": name,
                "Kind": "Variable",
                "Type/Return Type": dtype,
                "Value": value,
                "Memory": hex(id(value)) if value else "",
                "Parameters": "",
            }
        )

    def add_function(self, name, return_type, params):
        self.symbols.append(
            {
                "Name": name,
                "Kind": "Function",
                "Type/Return Type": return_type,
                "Value": "",
                "Memory": "",
                "Parameters": ", ".join(params) if params else "",
            }
        )

    def display(self):
        if self.symbols:
            print("\nSymbol Table:")
            print(tabulate(self.symbols, headers="keys", tablefmt="fancy_grid"))

    def process_code(self, code):
        # Match variable declarations with assignment
        for dtype, name, val in re.findall(
            r"\b(int|float|double|char|bool)\s+([a-zA-Z_]\w*)\s*=\s*([^;]+);", code
        ):
            self.add_variable(name, dtype, self.parse_value(dtype, val.strip()))

        # Match variable declarations without assignment
        for dtype, name in re.findall(
            r"\b(int|float|double|char|bool)\s+([a-zA-Z_]\w*)\s*;", code
        ):
            self.add_variable(name, dtype, None)

        # Match function declarations
        for ret_type, name, params in re.findall(
            r"\b(int|float|double|char|bool|void)\s+([a-zA-Z_]\w*)\s*\(([^)]*)\)\s*\{",
            code,
        ):
            self.add_function(
                name, ret_type, [p.strip() for p in params.split(",")] if params else []
            )

    def parse_value(self, dtype, val):
        val = val.strip()
        return (
            int(val)
            if dtype == "int"
            else (
                float(val)
                if dtype in ["float", "double"]
                else (
                    val.strip("'")
                    if dtype == "char"
                    else val.lower() == "true" if dtype == "bool" else val
                )
            )
        )


if __name__ == "__main__":
    code = """
    int x = 10;
    float y = 42.8;
    char c = 'A';
    int test;
    bool flag = true;

    int add(int a, int b) {
        return a + b;
    }

    bool is_even(int n) {
        return n % 2 == 0;
    }
    """

    sym_table = SymbolTable()
    sym_table.process_code(code)
    sym_table.display()
