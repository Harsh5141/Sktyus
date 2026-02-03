# Function to check Armstrong number.
def is_armstrong(n):
    num_str=str(n)
    num_digits=len(num_str)
    sum_digits=sum(int(digit)**num_digits for digit in num_str)
    return n == sum_digits
num = 153
if is_armstrong(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")