num1 = float(input("Give me the first number: "))
num2 = float(input("Give me the second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "undefined (division by zero)"

print("Thank you!")
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} / {num2} = {division}")
print(f"{num1} * {num2} = {multiplication}")