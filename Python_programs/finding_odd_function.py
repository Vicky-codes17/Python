# Finding the Odd function using filter()
num = [3,2,4,5,6,7,8,9]
odd = list(filter(lambda n:n%2==1,num))
print(odd)