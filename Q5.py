print("1: Ceclsius to Fahrenheit")
print("2: Fahrenheit to Ceclsius")
print("3: Kelvin to Ceclsius")

choice = int(input("Please enter the converstion. 1, 2 or 3: "))
temperature = float(input("Enter the temperature: "))

if choice == 1:
    if temperature < 273.15:
        print("Invalid Input! Celsius values cannot be below absolute zero (-273.15°C). Please Try Again.") 
    else:
        ConvertedValue = (temperature * 9/5) + 32
        print("The converted temperature from Celsius to Fahreneheit is: ", round(ConvertedValue,2))

elif choice == 2:
    if temperature < 459.15:
        print("Invalid Input! Fahrenheir values cannot be below absolute zero (-459.67°F). Please try Again.")
    else:
        ConvertedValue = (temperature - 32) * (5/9)
        print("The converted temperature from Fahrenheit to Celsius is: ", round(ConvertedValue,2))

elif choice == 3:
    if temperature < 0:
        print("Invalid Output! Kelvin values cannot be absolute zero(OK). Please try Again.")
    else:
        ConvertedValue = (temperature - 273.15)
        print("The converted temperature from Kelvin to Celsius is: ", round(ConvertedValue,2))
else:
    print("Invalid choice")




