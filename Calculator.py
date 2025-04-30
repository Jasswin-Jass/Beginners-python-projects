def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

opperations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculate():
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in opperations:
            print(symbol)
        opperation_symbol = input("Pick an operation?: ")
        num2 = float(input("What is the next number?: "))
        answer = opperations[opperation_symbol](num1,num2)
        print(f"{num1} {opperation_symbol} {num2} =  {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer},or type 'n' to do new operation: ")

        if choice == 'y':
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 50)
            calculate()

calculate()