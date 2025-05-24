def peephole_optimization(code):
    optimized = []
    for line in code:
        lhs, rhs = [x.strip() for x in line.split('=')]

        if '+' in rhs and rhs.endswith('+ 0'):
            var = rhs.split('+')[0].strip()
            optimized.append(f"{lhs} = {var}")
        elif '*' in rhs and rhs.endswith('* 1'):
            var = rhs.split('*')[0].strip()
            optimized.append(f"{lhs} = {var}")
        elif '*' in rhs and rhs.endswith('* 2'):
            var = rhs.split('*')[0].strip()
            optimized.append(f"{lhs} = {var} + {var}")
        elif lhs == rhs:
            continue
        else:
            optimized.append(line)
    return optimized


code = [
    "a = b",
    "c = a",
    "a = a",
    "d = c + 0",
    "e = d * 1",
    "f = e * 2"
]

optimized_code = peephole_optimization(code)

print("Optimized Code:\n")
for line in optimized_code:
    print(line)