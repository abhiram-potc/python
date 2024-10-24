def first_and_last(string):
    start=string[0]
    end=string[-1]
    new_string=end+string[1:-1]+start
    return new_string
string=input("Enter the string: ")
result = first_and_last(string)
print(f"new string: {result}")