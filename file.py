class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return 'Stack is empty'


def get_precedence(operator):
    """Get the precedence of an operator."""
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3
    }
    return precedence.get(operator, 0)


def is_operator(char):
    """Check if a character is an operator."""
    operators = ['+', '-', '*', '/', '^']
    return char in operators


def is_operand(char):
    """Check if a character is an operand."""
    return char.isalnum()


def infix_to_postfix(infix_expression):
    """Convert an infix expression to postfix."""
    stack = Stack()
    postfix_expression = ""

    for char in infix_expression:
        if is_operand(char):
            postfix_expression += char 
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while stack.peek() != '(':
                postfix_expression += stack.pop() 
            stack.pop()  # Remove the '('
        else:
            while not stack.is_empty() and stack.peek() != '(' and get_precedence(char) <= get_precedence(stack.peek()):
                postfix_expression += stack.pop() 
            stack.push(char)

    while not stack.is_empty():
        postfix_expression += stack.pop() 

    return postfix_expression.strip()


# Example usage:
infix_expression = input("enter your infix expression: ")
postfix_expression = infix_to_postfix(infix_expression) #a+b*c^d-f/g+g
print(f"Infix: {infix_expression}")
print(f"Postfix: {postfix_expression}") #abcd^*+fg/-g+
