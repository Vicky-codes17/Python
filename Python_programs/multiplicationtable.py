#Getting unput from user
number = int(input("Enter the number to print its multiplication table :"))

#Printing the multiplication table
print(f"Multiplication table for the {number} is :")
for i in range(1,11):
    print(f"{number} x {i} = {number * i}")