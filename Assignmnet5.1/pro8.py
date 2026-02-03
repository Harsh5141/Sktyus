# Function to find GCD of two numbers.
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
num1=33
num2=81
print("Gcd:",gcd(num1,num2))