number1 = int(input("Enter the first number:"))
number2 = int(input("Enter the Select number:"))
select = input("Choose the operation (+, -, *, /):")
result = 0

match select:
    case "+":
        result = number1 + number2
        print(f"The result is {result}")
    case "-":
        result = number1 - number2
        print(f"The result is {result}")
    case "*":
        result = number1 * number2
        print(f"The result is {result}")
    case "/":
        if number2 == 0:
            print("Division by zero is not allowed")
        else:
          result = number1 / number2
          print(f"The result is {result}")
    case _:
        print("invalid operation")