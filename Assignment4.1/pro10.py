a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Triangle is Equilateral")
    elif a == b or b == c or c == a:
        print("Triangle is Isosceles")
    else:
        print("Triangle is Scalene")
else:
    print("Not a valid triangle")
