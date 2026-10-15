RAMA_HEIGHT = 1.3
RAJA_HEIGHT = 1.7
if RAMA_HEIGHT > RAJA_HEIGHT:
    print("rama is taller: ")
else:
    print("raja is taller:")

total = float(input("enter total purchase amount: "))
if total >= 1000:
    discount = total * 0.10
    final_amount = total - discount 
    print ("discount applied:", discount)
    print ("final amount to pay:", final_amount)
else:
    print ("no discount applied")
    print ("total amount :",total)