weight = float(input("enter weight in kg:"))
height = float(input("enter height in meters:"))
bmi = weight / (height ** 2)
if bmi < 18.5:
    category = "underweight"
elif bmi > 25:
    category = "normal"
elif bmi > 30:
    category = "overweight"
else: category = "obese"
print("bmi:",bmi)
print("category:",category)

units = int(input("enter number units used:"))
if units <= 100:
    bill = units * 1
elif units <= 200:
    bill = 100 * 1 + (units - 100) * 2
else:
    bill = 100 * 1 + 100 * 2 + (units - 200) * 5
    print("electricity bill:",bill)

    a = int(input("enter first angle:"))
    b = int(input("enter second angle:"))
    c = int(input("enter third angle:"))

    if a == b and b == c == a:
        print("equilateral triangle")
    elif a == b or b == c or a == c:
        print("isosceles triangle")
    else:
        print("scalene triangle")