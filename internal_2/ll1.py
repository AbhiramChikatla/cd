from collections import defaultdict

def get_symbols(grammar):
    terminals = set()
    non_terminals = set(grammar.keys())
    for rules in grammar.values():
        for rule in rules:
            for symbol in rule:
                if not symbol.isupper() and symbol != 'ε':
                    terminals.add(symbol)
    terminals.add('$')  # End-of-input symbol
    return terminals, non_terminals

def compute_first_sets(grammar, terminals, non_terminals):
    first = {nt: set() for nt in non_terminals}

    def first_of(symbol):
        if symbol in terminals:
            return {symbol}
        if symbol == 'ε':
            return {'ε'}
        result = set()
        for rule in grammar[symbol]:
            for s in rule:
                sub_first = first_of(s)
                result.update(sub_first - {'ε'})
                if 'ε' not in sub_first:
                    break
                else:
                   result.add('ε')
        return result

    for nt in non_terminals:
        first[nt] = first_of(nt)
    return first

def compute_follow_sets(grammar, terminals, non_terminals, first_sets):
    follow = {nt: set() for nt in non_terminals}
    follow[next(iter(grammar))].add('$')  # Start symbol

    changed = True
    while changed:
        changed = False
        for nt, rules in grammar.items():
            for rule in rules:
                trailer = follow[nt].copy()
                for symbol in reversed(rule):
                    if symbol in non_terminals:
                        if trailer - follow[symbol]:
                            follow[symbol].update(trailer)
                            changed = True
                        if 'ε' in first_sets[symbol]:
                            trailer.update(first_sets[symbol] - {'ε'})
                        else:
                            trailer = first_sets[symbol]
                    else:
                        trailer = {symbol}
    return follow

def construct_parsing_table(grammar, terminals, non_terminals, first_sets, follow_sets):
    table = {nt: {t: '' for t in terminals} for nt in non_terminals}
    for nt, rules in grammar.items():
        for rule in rules:
            first_of_rule = set()
            for symbol in rule:
                first_of_symbol = first_sets[symbol] if symbol in first_sets else {symbol}
                first_of_rule.update(first_of_symbol - {'ε'})
                if 'ε' not in first_of_symbol:
                    break
                else:
                    first_of_rule.add('ε')

            for terminal in first_of_rule:
                if terminal != 'ε':
                    table[nt][terminal] = rule

            if 'ε' in first_of_rule:
                for terminal in follow_sets[nt]:
                    table[nt][terminal] = rule
    return table

def print_sets(title, sets):
    print(f"\n{title}:")
    for key, value in sets.items():
        print(f"{key}: {value}")

def print_parsing_table(parsing_table, terminals):
    print("\nLL(1) Parsing Table:")
    print("\t" + "\t".join(terminals))
    for nt, row in parsing_table.items():
        print(nt, end="\t")
        for t in terminals:
            print("".join(row[t]) if row[t] else "-", end="\t")
        print()

# **Modified Grammar (No Left Recursion, No Left Factoring, Unambiguous)**
grammar = {
    'E': [['T', "E'"]],
    "E'": [['+', 'T', "E'"], ['ε']],  # E → T E' | ε
    'T': [['F', "T'"]],
    "T'": [['*', 'F', "T'"], ['ε']],  # T → F T' | ε
    'F': [['id'], ['(', 'E', ')']]   # F → id | ( E )
}

# Compute necessary data
terminals, non_terminals = get_symbols(grammar)
first_sets = compute_first_sets(grammar, terminals, non_terminals)
follow_sets = compute_follow_sets(grammar, terminals, non_terminals, first_sets)
parsing_table = construct_parsing_table(grammar, terminals, non_terminals, first_sets, follow_sets)

# Print outputs
print_sets("First Function", first_sets)
print_sets("Follow Function", follow_sets)
print_parsing_table(parsing_table, terminals)