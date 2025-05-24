grammar = {
    "E":  [["T", "E'"]],
    "E'": [["+", "T", "E'"]],
    "T":  [["F", "T'"]],
    "T'": [["*", "F", "T'"]],
    "F":  [["(", "E", ")"], ["id"]]
}


first_sets = {}
follow_sets = {nt: set() for nt in grammar}

def first(symbol):
    if symbol not in grammar:
        return {symbol}  # Terminal

    if symbol in first_sets:
        return first_sets[symbol]

    first_set = set()
    for rule in grammar[symbol]:
        first_set |= first(rule[0])  # FIRST of first symbol
    first_sets[symbol] = first_set
    return first_set

def follow():
    follow_sets["E"].add('$')  # Start symbol gets '$'

    for nt, rules in grammar.items():
        for rule in rules:
            for i in range(len(rule) - 1):  # Process symbols except last
                if rule[i] in grammar:  # Non-terminal
                    follow_sets[rule[i]] |= first(rule[i + 1])  # FIRST of next symbol
            
            # Last symbol gets FOLLOW of LHS
            if rule[-1] in grammar:
                follow_sets[rule[-1]] |= follow_sets[nt]

for nt in grammar:
    first(nt)
follow()

# Print FOLLOW sets
for nt, f_set in first_sets.items():
    print(f"FIRST({nt}) = {f_set}")
print(" - - - - - - - - - - ")
for nt, f_set in follow_sets.items():
    print(f"FOLLOW({nt}) = {f_set}")