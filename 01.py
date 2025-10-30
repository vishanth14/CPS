# Printing address
house_no = input("Enter House No: ")
street   = input("Enter Street: ")
city     = input("Enter City: ")
state    = input("Enter State: ")
pincode  = input("Enter Pincode: ")

print("\nYour Address is:")
print(house_no)
print(street)
print(city + ", " + state + " - " + pincode)