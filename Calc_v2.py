def calculator():
    print("\n--- Basic Calculator ---")
    print("Type any arithmetic expression")
    print("Type 'quit' to exit.\n")

    while True:
        expression = input("Enter expression: ")

        if expression.lower() == "quit":
            print("Exiting calculator. Goodbye!")
            break

        try:
            # Evaluate the arithmetic expression safely
            result = eval(expression, {"__builtins__": None}, {})
            print("Result:", result)
        except Exception as e:
            print("Error! Invalid expression:", e)

if __name__ == "__main__":
    calculator()
