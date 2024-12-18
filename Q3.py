num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
# input the first and second number

if num2 == 0:# case to check if second number if zero.
    print("Second Number cannot be 0.")
    num2 = int(input("Please enter the Second Number Again: "))
    # if num2 is zero, then the user has to input again

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1/num2
#doing the calulations for sum, differenece, multiplication, and division.

# Question 3 Part 1
print("For Question 3 Part 1: ")
print("The sum of the two numbers are: ", sum)
print("The difference of the two numbers are: ", difference)
print("The product of the two numbers are: ", product)
print("The division of the two numbers are: ", quotient)
# printing the messages

# Question 3 Part 2
print("For Question 3 Part 2: ")
remainder = num1 % num2 # using modulo to get remainder
print("The remainder of the first number divided by the second number is: ", remainder)

# Question 3 Part 3
print("Question 3 Part 3")
power = pow(num1, num2)# using pow to put num1 to the power of num2
print("The first number raised to the second number", power)


print("Thank You.")



