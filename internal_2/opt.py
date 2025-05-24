import re

def constant_folding(lines):
    opt = []
    for line in lines:
        parts=line.split(" = ")
        if len(parts)==2:
            dst,expr=parts
            try:
                res=eval(expr)
                opt.append(f"{dst} = {res}")
            except:
                opt.append(line)
    return opt

def dead_code_elimination(lines):
    used_vars = set()
    # Collect all used variables on the right-hand side
    for line in lines:
        rhs = line.split(" = ")[-1]
        tokens = re.findall(r'\b\w+\b', rhs)
        used_vars.update(tokens)

    optimized = []
    for line in lines:
        lhs = line.split(" = ")[0].strip()
        # Keep the line if the variable is used or not an assignment
        if lhs in used_vars or re.match(r"[a-zA-Z]+\s*=\s*[^=]+", line) is None:
            optimized.append(line)
    return optimized

def common_subexpression_elimination(lines):
    expr_map = {}  # Maps expression to variable
    optimized = []

    for line in lines:
        match = re.match(r"(\w+)\s*=\s*(.*)", line)
        if match:
            var, expr = match.groups()
            if expr in expr_map:
                optimized.append(f"{var} = {expr_map[expr]}")
            else:
                expr_map[expr] = var
                optimized.append(line)
        else:
            optimized.append(line)
    return optimized

def read_code_file(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def main():
    filename = input("Enter the input code filename: ")
    lines = read_code_file(filename)

    print("\nOriginal Code:")
    for line in lines:
        print("\t" + line)

    lines = constant_folding(lines)
    lines = dead_code_elimination(lines)
    lines = common_subexpression_elimination(lines)

    print("\nOptimized Code:")
    for line in lines:
        print("\t" + line)

if __name__ == "__main__":
    main()
