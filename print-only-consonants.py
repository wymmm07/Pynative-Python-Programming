# Accept a string from the user
input_string = input("Enter a string: ")
print("Orginal String is", input_string)
print("Printing only consonant letters")
# Display consonant letters
consonant_letters = [char for char in input_string if char.isalpha() and char.lower() not in 'aeiou']
for char in consonant_letters:
    print(char)
