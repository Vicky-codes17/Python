#Getting the start and end of the interval
start = int(input("Enter the start of the interval :"))
end   = int(input("Enter the end of the interval :"))

print(f"Prime numbers between {start} and {end} are : ")

#For Loop 
for num in range(start,end + 1):
    if num > 1:
        is_prime = True
    #check if the number has any divisors
        for i in range(2,num):
            if num%i==0:
                is_prime = False
            break
        #If no divisors were found,the num is prime
        if is_prime:
            print(num)
