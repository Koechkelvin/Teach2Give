def capitalize_first_letter(sentence):
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

input_string = input("Enter a string: ")
result = capitalize_first_letter(input_string)
print("Result:", result)
