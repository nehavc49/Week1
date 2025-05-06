# User input
temp_type = input("Convert from (C)elsius or (F)ahrenheit? ").lower()
# Convert based on user choice
if temp_type == 'c':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is {fahrenheit}°F")
elif temp_type == 'f':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F is {celsius}°C")
else:
    print("Invalid input. Please enter 'C' or 'F'.")
