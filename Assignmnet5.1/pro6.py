# Function to count vowels in a string.
def count_vowels(s):
    vowels="aeiouAEIOU"
    count=0
    for ch in s:
        if ch in vowels:
            count+=1
    return count
text="Meet Patel"
print(count_vowels(text))