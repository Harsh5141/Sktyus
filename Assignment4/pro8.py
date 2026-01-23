#8 Find sum of even numbers between 1–100.
sum=0
for i in range(1,100):
    if i %2 ==0:
        sum += i
print(sum)