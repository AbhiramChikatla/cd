import re
from tabulate import tabulate

class TACGenerator:
    def __init__(self, expression):
        self.tokens = re.findall(r'\d+|[a-zA-Z]+|[-+*/=()]', expression)
        self.pos = 0
        self.temp_count = 0
        self.quadruples = []

    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consume(self):
        self.pos += 1
        return self.tokens[self.pos - 1]

    def factor(self):
        if self.peek() == '-':
            self.consume()
            operand = self.factor()
            temp = self.new_temp()
            self.quadruples.append(['-', operand, None, temp])
            return temp
        elif self.peek() == '(':
            self.consume()  # consume '('
            expr = self.expression()
            self.consume()  # consume ')'
            return expr
        else:
            return self.consume()

    def term(self):
        left = self.factor()
        while self.peek() in ('*', '/'):
            op = self.consume()
            right = self.factor()
            temp = self.new_temp()
            self.quadruples.append([op, left, right, temp])
            left = temp
        return left

    def expression(self):
        left = self.term()
        while self.peek() in ('+', '-'):
            op = self.consume()
            right = self.term()
            temp = self.new_temp()
            self.quadruples.append([op, left, right, temp])
            left = temp
        return left

    def parse(self):
        var = self.consume()  # Get the variable name
        self.consume()        # Consume '='
        expr = self.expression()
        self.quadruples.append(['=', expr, None, var])
        return self.quadruples

# Example usage
if __name__ == "__main__":
    exp =  "a=b*c+d"
    tac = TACGenerator(exp)
    quadruples = tac.parse()
    print(tabulate(quadruples, headers=["Op", "Arg1", "Arg2", "Result"], tablefmt="fancy_grid"))