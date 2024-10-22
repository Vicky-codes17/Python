#Find the largest number among three numbers

#Getting input from user
num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))
num3 = float(input("Enter the third number : "))

#Finding the largest number
if num1>=num2 and num1>=num3:
    largest = num1
elif num2>=num1 and num2>=num3:
    largest = num2
else:
    largest = num3

#Disaplay the result
print("The largest number is : ",largest)