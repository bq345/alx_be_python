number_1 = int(input("Enter the first number:"))
number_2 = int(input("Enter the Select number:"))
select = input("Choose the operation (+, -, *, /):")
result = 0

match select:
    case "+":
        result = number_1 + number_2
        print(f"The result is {result}")
    case "-":
        result = number_1 - number_2
        print(f"The result is {result}")
    case "*":
        result = number_1 * number_2
        print(f"The result is {result}")
    case "/":
        if number_2 == 0:
            print("Division by zero is not allowed")
        else:
          result = number_1 / number_2
          print(f"The result is {result}")
    case _:
        print("invalid operation")