first_number  = int(input("Enter first number: "))
math_operation = input("Choose an operand +, -, *, /: ")
second_number = int(input("Enter second number: "))

if math_operation == "+":
    print(first_number + second_number)
if math_operation == "-":
    print(first_number - second_number)
if math_operation == "*":
    print(first_number * second_number)
if math_operation == "/":
    print(first_number / second_number)    
