# import python string module to enable translate function
import string


# function for counting the characters
def count_characters(s):
    # empty dictionary to hold key and value
    count = {}
    # for loop to loop through the parameter characters
    for i in s:
        # condition to check if the character is present in the dictionary created
        if i in count:
            # if the character is present, its value is increased by 1
            count[i] += 1
        # if the character is not present in the dictionary created
        else:
            # its given a value of 1
            count[i] = 1
    # displays the dictionary's keys and values
    print(count)


# collects user input, converts them to uppercase characters and stores it in user_inputs variable
user_inputs = input(">_").upper()
# the function created above is called here and user_inputs is passed as an argument.
# using translate method, it removes all the white-spaces from the string and results in a compact string as output.
count_characters(user_inputs.translate({ord(c): None for c in string.whitespace}))
