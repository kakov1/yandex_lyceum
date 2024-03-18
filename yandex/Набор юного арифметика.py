def arithmetic_operation(operation):
    def operation_(a, b):
        if operation == '+':
            return a + b
        elif operation == '-':
            return a - b
        elif operation == '*':
            return a * b
        else:
            return a / b
    return operation_
