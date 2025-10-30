# Speed unit conversion (kmph to mph)
print("Select Conversion:")
print("1. Kilometer to Miles")
print("2. Miles to Kilometer")

choice = input("Enter your choice (1 or 2): ")

if choice == '1':
    km = float(input("Enter distance in Kilometers: "))
    miles = km * 0.621371
    print(f"{km} km = {miles:.2f} miles")
elif choice == '2':
    miles = float(input("Enter distance in Miles: "))
    km = miles / 0.621371
    print(f"{miles} miles = {km:.2f} km")
else:
    print("Invalid choice. Please select 1 or 2.")