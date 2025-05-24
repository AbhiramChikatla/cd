def loop_fusion(code_lines):
    fused_code = []
    i = 0

    while i < len(code_lines):
        line = code_lines[i].strip()

        if (i + 1 < len(code_lines)
            and line.startswith("for ")
            and code_lines[i + 1].strip().startswith("for ")
            and line.split(":")[0] == code_lines[i + 1].strip().split(":")[0]):

            loop_header = line.split(":")[0] + ":"
            body1 = line.split(":")[1].strip()
            body2 = code_lines[i + 1].strip().split(":")[1].strip()

            fused_code.append(loop_header)
            fused_code.append(f"    {body1}")
            fused_code.append(f"    {body2}")
            i += 2 
        else:
            fused_code.append(line)
            i += 1

    return fused_code

code_lines = [
    "for i in range(n): a[i] = b[i] + 1",
    "for i in range(n): c[i] = d[i] * 2",
    "print(a[0], c[0])"
]
code=loop_fusion(code_lines)
for line in code:
    print(line)