while True:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    num1 = float(num1)
    num2 = float(num2)

    result = num1 * num2

    print(f"{num1} x {num2} = {result}")

    if result > 0:
        print("The result is positive.")
    elif result < 0:
        print("The result is negative.")
    else:
        print("The result is zero.")
