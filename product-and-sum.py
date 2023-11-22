#Exercise 1: Calculate the multiplication and sum of two numbers
#Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
def display_number(number1, number2):
    #product
    prod = int(number1) * int(number2)
    #addition
    sum = int(number1) + int(number2)
    #result
    if prod <= 1000:
       print("The product of num1 and num2 is: ", prod)
    else:
       print("The sum of num1 and num2 is: ", sum)

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
display_number(number1, number2)

