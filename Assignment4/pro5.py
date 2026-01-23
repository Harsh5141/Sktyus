#5 Check if a number is prime.
num=int(input("Enter a number: "))
count = 0
for i in range(1,num+1):
    if num % i ==0:
        count +=1
if count == 2:
    print("prime is number")
else:
    print("Not prime is number")