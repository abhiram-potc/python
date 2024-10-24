def find_longest_word(words):
    if not words:
        return None

    longest_word = words[0]

    for word in words[1:]:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word

user_words = []

num_words = int(input("How many words would you like to enter? "))

for i in range(num_words):
    word = input(f"Enter word {i + 1}: ")
    user_words.append(word)

longest = find_longest_word(user_words)

if longest:
    print(f"The longest word is: {longest}")
else:
    print("No words were entered.")