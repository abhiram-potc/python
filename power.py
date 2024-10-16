def power(a,b):
    if b==0:
        return 1
    elif b<0:
        return 1/power(a,-b)
    else:
        return a*power(a, b-1)
a=int(input("Enter 1st digit: "))
b=int(input("Enter power: "))
result=power(a,b)
print(f"{a} ** {b} = {result}")