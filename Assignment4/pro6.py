    
#6 Reverse a number (e.g., 123 → 321).
num = int(123)
rev =0
while num > 0:
    digit = num %10
    rev = rev * 10 + digit
    num//=10
print("Reverse num: ",rev)
