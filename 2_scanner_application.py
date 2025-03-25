import re

KEYWORDS = {"if", "else", "while", "for", "return", "int", "float", "char", "void", "break", "continue"}
OPERATORS = {"+", "-", "*", "/", "=", "==", "!=", "<", ">", "<=", ">=", "&&", "||", "!"}
DELIMITERS = {";", ",", "(", ")", "{", "}"}

def is_identifier(token):
    return re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', token) is not None

def is_number(token):
    return re.match(r'^\d+(\.\d+)?$', token) is not None

def tokenize_line(line):
    tokens = re.split(r'(\s+|[;,\(\)\{\}])', line)  
    return [token for token in tokens if token.strip()]  

def classify_token(token):
    if token in KEYWORDS:
        return "KEYWORD"
    elif token in OPERATORS:
        return "OPERATOR"
    elif token in DELIMITERS:
        return "DELIMITER"
    elif is_number(token):
        return "NUMBER"
    elif is_identifier(token):
        return "IDENTIFIER"
    else:
        return "UNKNOWN"

def scanner(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            
            print(f"{'Token':<15} {'Type':<15}")
            print("-" * 30)

            for line_num, line in enumerate(lines, start=1):
                tokens = tokenize_line(line)
                for token in tokens:
                    token_type = classify_token(token)
                    print(f"{token:<15} {token_type:<15}")

    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = 'sample.txt'  
scanner(file_path)
