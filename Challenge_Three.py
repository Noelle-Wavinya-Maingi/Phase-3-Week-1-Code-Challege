# define a function to calculate the highest value of consonant substring
# define a string containing the vowels and alphebets for position calculation
def consonant_value(string):
    vowels = 'aeiou'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    new_string = ''
    # iterate through each character in the input string replacing the vowels with |
    for char in string.lower():
        if char in vowels:
            new_string += '|'
        else:
            new_string += char

# split the new string into a list of consonant sequences
    string_list = new_string.split('|')
    print("The string list without vowels is:", string_list)

    char_value_list = []

# calculate the value of each consonant sequence and store in a list named char_value_list after calculating the sum of the positions in the alphabet.
    for chars in string_list:
        char_value = sum([alphabet.find(char) + 1 for char in chars])
        char_value_list.append(char_value)

# return the maximum value among the calculated values
    return max(char_value_list)


# a loop that checks the input a user has entered is valid
while True:
    input_string = input("Enter a string: ")
    if input_string.isalpha():
        break
    else:
        print("Enter a valid input that does not have special characters")


# call the function to calculate and print the highest value of consonant substrings
result = consonant_value(input_string)
print(f'Highest consonant value in {input_string} is:', result)
