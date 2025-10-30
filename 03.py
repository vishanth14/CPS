#Temperature unit conversion (Celsius to Fahrenheit)
print("Select Conversion:")
print("1. Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")

choice = input("Enter your choice (1 or 2): ")

if choice == '1':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit}°F = {celsius:.2f}°C")
elif choice == '2':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius}°C = {fahrenheit:.2f}°F")
else:
    print("Invalid choice. Please select 1 or 2.")