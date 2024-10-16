def loop_through_characters():
    string = input("Enter a string: ")
    count_a = 0
    for char in string:
        if char == 'a':
            count_a += 1
    print(f"The character 'a' occurs {count_a} times in the string.")
loop_through_characters()