# Define the calculator tool that Claude is allowed to request.
CALCULATOR_TOOL = {
    "name": "calculate",
    "description": "Perform basic arithmetic using two numbers.",
    "input_schema": {
        "type": "object",
        "properties": {
            "a": {"type": "number"},
            "b": {"type": "number"},
            "operation": {
                "type": "string",
                "enum": ["add", "subtract", "multiply", "divide"]
            }
        },
        "required": ["a", "b", "operation"]
    }
}

# Perform one basic arithmetic operation.
def calculate(a, b, operation):
    if operation == "add":
        return a + b

    if operation == "subtract":
        return a - b

    if operation == "multiply":
        return a * b

    if operation == "divide":
        if b == 0:
            return "Cannot divide by zero."
        return a / b

    return "Unknown operation."