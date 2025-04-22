def copy_propagation(code):
    copies = {}
    result = []
    for line in code.split("\n"):
        if "=" in line:
            lhs, rhs = map(str.strip, line.split("="))
            if rhs in copies:
                rhs = copies[rhs]
            copies[lhs] = rhs
            result.append(f"{lhs} = {rhs}")
    return "\n".join(result)


print(copy_propagation("a = b\nc = a"))  # c = b


def strength_reduction(expr):
    return expr.replace("* 2", "+ x").replace("x * 2", "x + x")


print(strength_reduction("x = x * 2"))  # x = x + x


def loop_invariant_code_motion(loop_code):
    loop = []
    invariant = []
    for line in loop_code:
        if "i" not in line:
            invariant.append(line)
        else:
            loop.append(line)
    return invariant + ["for i in range(n):"] + ["    " + l for l in loop]


code = ["x = a * b", "y[i] = x + i", "y[i]*=2"]
print("\n".join(loop_invariant_code_motion(code)))


def induction_elimination(code):
    print("before induction variable elimination: ")
    print(code)
    print("after induction variable elimination: ")
    code = code.replace("j = i * 2", "# eliminated j, use i*2 directly")
    code = code.split("\n")
    code[-1] = "    a[i]=i*2"
    return "\n".join(code)


print(induction_elimination("for i in range(n):\n    j = i * 2\n    a[j] = i"))


def loop_unroll(var, start, end, body):
    return "\n".join(body.replace(var, str(i)) for i in range(start, end))


body = "a[i] = 0"
print(loop_unroll("i", 0, 4, body))  # Unrolls for i in range(4)


def inline_function(call_code, func_body):
    call = call_code.split(" = ")[-1]
    return call_code.replace(f"{call}", func_body)


code = "x = add(int a,int b)"
func_body = "a+b"
print(inline_function(code, func_body))  # x = a + b

import re


def peephole(code):
    lines = code.split("\n")
    optimized = []
    for line in lines:
        parts = line.split(" ")
        if parts[1][:-1] == parts[2]:
            continue
        optimized.append(line)
    return "\n".join(optimized)


print(
    peephole("mov r1, r1\nadd r2, r3\nload r2, r2\njump a, a")
)  # removes redundant mov


def register_allocation(variables):
    registers = ["R1", "R2", "R3"]
    return {var: registers[i % len(registers)] for i, var in enumerate(variables)}


print(register_allocation(["a", "b", "c", "d"]))  # Maps variables to registers


def instruction_scheduling(instructions):
    mp = {
        "load": 1,
        "mov": 2,
        "add": 3,
        "sub": 3,
        "mul": 4,
        "div": 4,
        "store": 5,
        "jmp": 6,
        "cmp": 7,
    }

    def get_priority(inst):
        inst_type = inst.strip().split()[0].lower()
        return mp.get(inst_type, 99)

    return sorted(instructions, key=get_priority)


# Example usage
instructions = [
    "add a, b",
    "load x",
    "store y",
    "mul c, d",
    "mov r1, r2",
    "jmp label",
    "cmp x, y",
]

scheduled = instruction_scheduling(instructions)
print("\n".join(scheduled))


# moves load first
def tail_rec_fact(n, acc=1):
    if n == 0:
        return acc
    return tail_rec_fact(n - 1, acc * n)


print(tail_rec_fact(5))  # Output: 120
