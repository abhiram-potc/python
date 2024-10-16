def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a,b):
    if b==0:
        print("not possible")
    else:
        return a/b

def pow(a, b):
    return a ** b

def calc(op, a, b):
    if op == '+':
        return add(a, b)
    elif op == '-':
        return sub(a, b)
    elif op == '*':
        return mul(a, b)
    elif op == '/':
        return div(a, b)
    elif op == '**':
        return pow(a, b)
    else:
        print("Not recognized")
        exit(0)

a = int(input("Enter 1st digit: "))
op = input("+, -, *, /, **\nEnter any of the operations: ")
b = int(input("Enter 2nd digit: "))

result = calc(op, a, b)
print("Result:", result)