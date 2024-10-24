def replace(string):
    first=string[0]
    var=first
    for char in string[1:]:
        if char == first:
            var+='$'
        else:
            var+=char
    return var
string=input("Enter a string: ")
print(f"new string: {replace(string)}")