n = 121
sum = 0

while n!=0:
    digit = n%10
    sum += sum
    n = n//10
print(sum)