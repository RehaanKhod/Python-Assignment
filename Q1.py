n = int(input("Enter the size of the triangle: ")) # asks the user to enter the size of the triangle
while n < 1:
    print("Error, triangle size cannot by less than 1, please try again.")
    n = int(input("Enter the size of the triangle: ")) # triangle size cannot be less than 1, it then asks the user to enter the size of the triangle again.

for i in range(1, n+1): # for loop to iterate through the range of 1 to n+1
    space = n - i 
    pattern = 2*i-1 

    print(" " * space + "*" * pattern)# prints the space and pattern

for i in range(n-1, 0, -1):# for the loop to iterate  for the second half of the triangle
    space = n - i
    pattern = 2*i-1

    print(" "*space+"*"*pattern) # prints the seoond half of the triangle