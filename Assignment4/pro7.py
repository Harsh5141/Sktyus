#7 Count digits in a number.
n=int(input("enter a num: "))
count=0
while n > 0:
    count +=1
    n//=10
print("Digigts num: ",count)