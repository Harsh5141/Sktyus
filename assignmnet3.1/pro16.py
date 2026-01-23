#Count word frequency in a given string using a dictionary.
string=("harsh is a student meet live in valsad.")
words=string.split()
word_count={}
for word in words:
    word_count[word] = word_count.get(word, 0)+1
print(word_count)