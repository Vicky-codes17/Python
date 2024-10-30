def calculate_values(num1,num2):
    #input numbers
    num1 = 10
    num2 = 5
    #Calculate sum,difference & product
    sum = num1 + num2
    diff = num1 - num2
    prod = num1 * num2
    #Return all three values
    return sum,diff,prod
#Calling the function
result_sum,result_diff,result_prod = calculate_values(10,5)

#Displaying output
print("Sum : ",result_sum)
print("Difference : ",result_diff)
print("Product  :",result_prod)
