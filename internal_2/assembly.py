import re
def generate_assembly(lines):
    assembly = []
    for line in lines:
        match = re.match(r"(\w+)\s*:=\s*(\w+)\s*([\+\-\*/])\s*(\w+)", line)
        if match:
            dest, op1, operator, op2 = match.groups()
            assembly.append(f"LOAD R1, {op1}")
            assembly.append(f"{operator_to_instruction(operator)} R1, {op2}")
            assembly.append(f"STORE {dest}, R1")
        else:
            match = re.match(r"(\w+)\s*:=\s*(\w+)", line)
            if match:
                dest, src = match.groups()
                assembly.append(f"MOV {dest}, {src}")
            else:
                assembly.append(f"# Unable to parse: {line}")  # For unsupported formats
    return assembly
def operator_to_instruction(op):
    return {
        '+': 'ADD',
        '-': 'SUB',
        '*': 'MUL',
        '/': 'DIV'
    }[op]
def read_code_file(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines() if line.strip()]
def main():
    filename = input("Enter the input code filename: ")
    lines = read_code_file(filename)
    print("\nOriginal Code:")
    for line in lines:
        print("\t" + line)
    print("\nGenerated Assembly Code:")
    asm = generate_assembly(lines)
    for instr in asm:
        print("\t" + instr)
main()
