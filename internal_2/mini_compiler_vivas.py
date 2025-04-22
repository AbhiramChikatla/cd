import re

# Input
code = "x = 5 + 3 * 2"


# 1. Lexical Analysis
def lexical_analysis(code):
    tokens = re.findall(r"[a-zA-Z_]\w*|==|<=|>=|!=|[0-9]+|[+\-*/=()]", code)
    print("1. Lexical Analysis (Tokens):", tokens)
    return tokens


# 2. Syntax Analysis
def syntax_analysis(tokens):
    if tokens[1] != "=":
        raise SyntaxError("Expected '=' after identifier")
    print("\n2. Syntax Analysis (Parse Tree):")
    print("  Assignment")
    print("  ├── Identifier:", tokens[0])
    print("  └── Expression:", " ".join(tokens[2:]))
    return ("assign", tokens[0], tokens[2:])


# 3. Semantic Analysis
def semantic_analysis(ast):
    _, var, expr = ast
    for token in expr:
        if re.match(r"[a-zA-Z_]\w*", token) and token != var:
            raise NameError(f"Undeclared variable '{token}'")
    print("\n3. Semantic Analysis: PASSED")
    return True


# 4. Intermediate Code Generation
def intermediate_code(ast):
    _, var, expr = ast
    temp_counter = 1
    stack = []
    ops = {"+", "-", "*", "/"}
    postfix = infix_to_postfix(expr)
    code = []
    for token in postfix:
        if token not in ops:
            stack.append(token)
        else:
            b = stack.pop()
            a = stack.pop()
            temp = f"t{temp_counter}"
            code.append(f"{temp} = {a} {token} {b}")
            stack.append(temp)
            temp_counter += 1
    print("\n4. Intermediate Code (3AC):")
    for line in code:
        print(" ", line)
    return code


def infix_to_postfix(tokens):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}
    output, stack = [], []
    for token in tokens:
        if token.isnumeric() or token.isalpha():
            output.append(token)
        elif token in precedence:
            while stack and precedence.get(stack[-1], 0) >= precedence[token]:
                output.append(stack.pop())
            stack.append(token)
    while stack:
        output.append(stack.pop())
    return output


# 5. Code Optimization
def code_optimization(intermediate):
    optimized = []
    for line in intermediate:
        parts = line.split(" = ")
        if len(parts) == 2:
            dest, expr = parts
            try:
                result = eval(expr)
                optimized.append(f"{dest} = {result}")
            except:
                optimized.append(line)
    print("\n5. Code Optimization:")
    for line in optimized:
        print(" ", line)
    return optimized


# 6. Code Generation (Assembly)
def code_generation(optimized_code):
    print("\n6. Code Generation (Assembly Output):")
    for line in optimized_code:
        dest, expr = line.split(" = ")
        parts = expr.split()
        if len(parts) == 1:
            print(f"  MOV {dest}, {parts[0]}")
        elif len(parts) == 3:
            op1, operator, op2 = parts
            print(f"  MOV R1, {op1}")
            if operator == "+":
                print(f"  ADD R1, {op2}")
            elif operator == "-":
                print(f"  SUB R1, {op2}")
            elif operator == "*":
                print(f"  MUL R1, {op2}")
            elif operator == "/":
                print(f"  DIV R1, {op2}")
            print(f"  MOV {dest}, R1")


# Run all phases
tokens = lexical_analysis(code)
ast = syntax_analysis(tokens)
semantic_analysis(ast)
intermediate = intermediate_code(ast)
optimized = code_optimization(intermediate)
code_generation(optimized)
