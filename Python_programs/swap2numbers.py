#Getting input from user
num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))

#Display the user entered numbers
print(f"Before swapping num1 = {num1}, num2 = {num2}")

#Swapping without a temporary variable
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

#Display the swapped numbers
print(f"After swapping num1 = {num1}, num2 = {num2}")