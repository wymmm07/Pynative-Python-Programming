# Accept a string from the user
input_string = input("Enter a string: ")
# Print the original string
print("Original String is", input_string) 
# Display characters at even index numbers
even_index_characters = [input_string[i] for i in range(0, len(input_string), 2)]
for char in even_index_characters:
    print(char)
