p=1000
t=1
r=10
ci=p*(1+(r/100))**t-p
print(ci)

phy=90
bio=80
eng=90
avg=(phy+bio+eng)/3
print(avg)

a=10
b=20
print("before swapping:")
print("a=",a)
print("b=",b)

a,b=b,a
print("after swapping:")
print("a=",a)
print("b=",b)

