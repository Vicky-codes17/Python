#Getting input from the first complex number
real1 = float(input("Enter the real part of first complex number : "))
imag1 = float(input("Enter the imaginary part of second complex number :"))

complex1 = complex(real1,imag1)
#Getting input from user of the second complex number
real2 = float(input("Enter the real part of the second complex number : "))
imag2 = float(input("Enter the imaginary part of the second complex number :"))

complex2 = complex(real2,imag2)

#Sum & Product of two complex number
sum_result = complex1 + complex2
product_result = complex1 * complex2

print(f"The Sum of {complex1} and {complex2} is {sum_result}")
print(f"The Product of {complex1} and {complex2} is {product_result}")