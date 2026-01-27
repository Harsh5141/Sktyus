unit = int(input("Enter bill units: "))

if unit <= 100:
    bill = unit * 7.3

elif unit <= 200:
    bill = (100 * 7.3) + ((unit - 100) * 7.3) + 150

elif unit <= 300:
    bill = (200 * 7.3) + ((unit - 200) * 7.3) + 350

elif unit <= 400:
    bill = (300 * 7.3) + ((unit - 300) * 7.3) + 500

elif unit <= 500:
    bill = (400 * 7.3) + ((unit - 400) * 7.3) + 800

else:
    bill = (500 * 7.3) + ((unit - 500) * 7.3) + 1000

print("Electricity Bill:", bill)
