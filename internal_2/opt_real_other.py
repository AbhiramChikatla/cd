import re


# Evaluate constant expressions at compile time.
def constant_folding(lines):
    opt = []
    for line in lines:
        parts = line.split(" = ")
        if len(parts) == 2:
            dst, expr = parts
            try:
                res = eval(expr)
                opt.append(f"{dst} = {res}")
            except:
                opt.append(line)
    return opt


lines = ["a = 2 + 3"]
val = constant_folding(lines)


# the code is said to dead when the statements that compute values that never get used
def dead_code_elimination(lines):
    used_vars = set()
    # Collect all used variables on the right-hand side
    for line in lines:
        rhs = line.split(" = ")[-1]
        tokens = re.findall(r"\b\w+\b", rhs)
        used_vars.update(tokens)

    optimized = []
    for line in lines:
        lhs = line.split(" = ")[0].strip()
        # Keep the line if the variable is used or not an assignment
        if lhs in used_vars or re.match(r"[a-zA-Z]+\s*=\s*[^=]+", line) is None:
            optimized.append(line)
    return optimized


lines = ["a = 5", "b = a + 3", "c = b * 2", "d = 10", "e = f + 1", "print(c)"]
val = dead_code_elimination(lines)


# An occurrence of an expression E is called a common sub expression if E was previously computed and the values of variables in E have not changed since the previous computation.
# And the common sub expressions are eliminated
def common_subexpression_elimination(lines):
    expr_map = {}  # Maps expression to variable
    optimized = []

    for line in lines:
        parts = line.split(" = ")
        if len(parts) == 2:
            var, expr = parts
            if expr in expr_map:
                optimized.append(f"{var} = {expr_map[expr]}")
            else:
                expr_map[expr] = var
                optimized.append(line)
        else:
            optimized.append(line)
    return optimized


lines = ["a = x + y", "b = x + y", "c = a * 2", "d = x + y", "e = c + 1", "f = a * 2"]
val = common_subexpression_elimination(lines)


# An assignment statement in the form f :=g called copy statement.
# The idea behind the copy propagation is to use g for f wherever possible after the copy statement f :=g


def copy_propagation(lines):
    copies = {}
    opt_code = []
    for line in lines:
        if "=" in line:
            lhs, rhs = map(str.strip, line.split("="))
            if rhs in copies:
                rhs = copies[rhs]
            copies[lhs] = rhs
            opt_code.append(f"{lhs} = {rhs}")
    return opt_code


lines = [
    "a = b",
    "i = x",
    "c = a",
    "j = i",
]
val = copy_propagation(lines)


def strength_reduction(expr):
    return expr.replace("* 2", "+ x").replace("x * 2", "x + x")


# print(strength_reduction("x = x * 2"))


def main():
    def loop_invariant_code_motion(loop_code, loop_variable):
        loop = []
        invariant = []
        for line in loop_code:
            if loop_variable in line:
                loop.append(line)
            else:
                invariant.append(line)
        return [l for l in invariant] + [loop_statement] + ["  " + l for l in loop]

    loop_code = ["a+=b*2", "x[i]-=1", "y[i]=y[i]**2", "val+=1"]
    loop_variable = "i"
    loop_statement = "for i in range(n)"
    print("Before : -------------------------")
    print(loop_statement)
    for l in loop_code:
        print("\t" + l)
    new_code = loop_invariant_code_motion(loop_code, loop_variable)
    print("After : ------------------------- ")

    for l in new_code:
        print(l)


def main():
    def loop_unroll(var, start, end, body):
        return "\n".join(body.replace(var, str(i)) for i in range(start, end))

    body = "a[i]+=1"
    print(loop_unroll("i", 0, 4, body))


def main():

    def loop_fission(lines):
        loop_a = []
        loop_b = []
        for ind, line in enumerate(lines):
            if "for" in line:
                loop_a.append(loop_statement)
                loop_b.append(loop_statement)
            else:
                if ind & 1:
                    loop_a.append(line)
                else:
                    loop_b.append(line)
        return loop_a + loop_b

    input_code = ["for i in range(N):", "    x := x + 1", "    y := y + 2"]

    loop_statement = input_code[0]

    output_code = loop_fission(input_code)
    for line in output_code:
        print(line)

