#10 Find all divisors of a number.
num=10
for i in range(1,num+1):
    if num % i ==0:
        print(i)