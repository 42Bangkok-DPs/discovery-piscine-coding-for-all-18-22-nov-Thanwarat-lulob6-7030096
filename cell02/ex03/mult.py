while True:
    num1 = input("Enter the first number: ")
    if num1.lower() == 'exit':
        break

    num2 = input("Enter the second number: ")
    if num2.lower() == 'exit':
        break

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
