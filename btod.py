n=input("Enter binary digit: ")
dec=0
is_valid = True
for bi in n:
    if bi not in '01':
        is_valid = False
        break;
if is_valid:
    for bi in n:
        dec=dec*2+ int(bi)
    print("The decimal is: ",dec)
else:
    print("Invalid")