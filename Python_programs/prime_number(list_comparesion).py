start = int(input("Enter the start of the interval :"))
end   = int(input("Enter the end of the interval :"))

print(f"Prime numbers between {start} and {end} are : ")

prime = [num for num in range(start,end+1)
              for i in range(2,num) if num%i==0]

print(prime)