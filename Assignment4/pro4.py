#4 Generate the first N Fibonacci numbers.
num = int(5)
a,b=0,1
for i in range(num):
    print(a)
    a,b = a+b,a
