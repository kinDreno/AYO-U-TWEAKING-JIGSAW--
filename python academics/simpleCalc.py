def calc():
    # Get the first and second numbers outside of the loop
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    
    while True:  # Start an infinite loop
        operator = input("Enter the operation (+ - * /): ")
        
        if operator == "+":
            return n1 + n2
        elif operator == "-":
            return n1 - n2
        elif operator == "*":
            return n1 * n2
        elif operator == "/":
                return n1 / n2
        else:
            print("Inputted an invalid operator, try again!")

# Call the function and print the result
print(calc())
