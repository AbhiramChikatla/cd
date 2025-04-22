import re

# -------------------- Phase 1: LEXICAL ANALYSIS --------------------
def lexer(code):
    token_spec = [
        ('NUMBER',   r'\d+'),
        ('ASSIGN',   r'='),
        ('ID',       r'[a-zA-Z_][a-zA-Z0-9_]*'),
        ('OP',       r'[+\-*/]'),
        ('NEWLINE',  r'\n'),
        ('SKIP',     r'[ \t]+'),
        ('MISMATCH', r'.'),
    ]
    token_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_spec)
    tokens = []
    for match in re.finditer(token_regex, code):
        kind = match.lastgroup
        value = match.group()
        if kind == 'NUMBER':
            value = int(value)
        elif kind in ('SKIP', 'NEWLINE'):
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f"Unexpected token: {value}")
        tokens.append((kind, value))
    return tokens

# -------------------- Phase 2: SYNTAX ANALYSIS --------------------
def parser(tokens):
    pos = 0
    ast = []

    def match(expected):
        nonlocal pos
        if pos < len(tokens) and tokens[pos][0] == expected:
            pos += 1
            return tokens[pos - 1][1]
        raise SyntaxError(f"Expected {expected}, got {tokens[pos]}")

    while pos < len(tokens):
        var = match('ID')
        match('ASSIGN')
        expr = []
        expr.append(match('NUMBER') if tokens[pos][0] == 'NUMBER' else match('ID'))

        while pos < len(tokens) and tokens[pos][0] == 'OP':
            op = match('OP')
            right = match('NUMBER') if tokens[pos][0] == 'NUMBER' else match('ID')
            expr.append(op)
            expr.append(right)

        ast.append(('assign', var, expr))
    return ast

# -------------------- Phase 3: SEMANTIC ANALYSIS --------------------
def semantic_analysis(ast):
    defined_vars = set()
    for node in ast:
        _, var, expr = node
        for item in expr:
            if isinstance(item, str) and item.isidentifier() and not item.isdigit() and item not in defined_vars:
                raise NameError(f"Semantic Error: Variable '{item}' used before assignment")
        defined_vars.add(var)

# -------------------- Phase 4 & 5: CODE GENERATION --------------------
def generate_code(ast):
    python_code = ""
    for node in ast:
        var = node[1]
        expr = ' '.join(str(e) for e in node[2])
        python_code += f"{var} = {expr}\nprint('{var} =', {var})\n"
    return python_code

# -------------------- Phase 6: EXECUTION --------------------
def compile_and_run(code):
    print("----- Lexical Analysis -----")
    tokens = lexer(code)
    # print(tokens)
    for ele in tokens:
        print(ele)

    print("\n----- Syntax Analysis (AST) -----")
    ast = parser(tokens)
    print(ast)

    print("\n----- Semantic Analysis -----")
    semantic_analysis(ast)
    print("Semantic check passed ✅")

    print("\n----- Code Generation -----")
    python_code = generate_code(ast)
    print(python_code)

    print("----- Execution Output -----")
    exec(python_code)

# -------------------- MAIN --------------------
if __name__ == "__main__":
    print("Enter your simple Python code (end with an empty line):")
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    
    user_code = "\n".join(lines)
    compile_and_run(user_code)