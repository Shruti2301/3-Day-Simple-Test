def count_vowels(text):
    count = 0
    vowels = "aeiouAEIOU"
    for char in text: 
        if char in vowels:
            count = count + 1
    return count 

# Pass a string prompt to input() so the user knows to type something
user_input = input("Enter a string: ")
print(count_vowels(user_input))