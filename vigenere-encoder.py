#!/usr/env/bin python


############################
# Vigenere Encoder.
# Made by TeknoBen96
# 10/21/2020
############################


# This array stores letters to be called during deciphering
alphabetic_array = [
    "a",    # 0
    "b",    # 1
    "c",    # 2
    "d",    # 3
    "e",    # 4
    "f",    # 5
    "g",    # 6
    "h",    # 7
    "i",    # 8
    "j",    # 9
    "k",    # 10
    "l",    # 11
    "m",    # 12
    "n",    # 13
    "o",    # 14
    "p",    # 15
    "q",    # 16
    "r",    # 17
    "s",    # 18
    "t",    # 19
    "u",    # 20
    "v",    # 21
    "w",    # 22
    "x",    # 23
    "y",    # 24
    "z",    # 25
]

# This array stores numeric values for coresponding letters
char_num = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
    "l": 11,
    "m": 12,
    "n": 13,
    "o": 14,
    "p": 15,
    "q": 16,
    "r": 17,
    "s": 18,
    "t": 19,
    "u": 20,
    "v": 21,
    "w": 22,
    "x": 23,
    "y": 24,
    "z": 25
    }


# Makes and returns an array with the code characters
def get_code_array():
    code = input("[+] Enter text here >>> ")
    code_len = len(code)
    code_array = []
    for i in range(0, code_len, 1):
        code_array.append(code[i])
    return code_array, code_len


# Makes and returns an array with the key characters
def get_key_array():
    key = input("[+] Enter key >>> ")
    key_len = len(key)
    key_array = []
    for i in range(0, key_len, 1):
        key_array.append(key[i])
    return key_array


# Converts code in to numeric values and returns then in an array
def numerate(code):
    numerated_array = []
    code_len = len(code)
    for i in range(0, code_len, 1):
        numerated_array.append(char_num[code[i]])
    return numerated_array


# Generates a repeating key for the length of the code, then returns it as an array
def generate_key(key, code_len):
    try_num = 0
    key_string = key
    for i in range(0, code_len, 1):
        key_string_len = len(key_string)
        if key_string_len < code_len:
            key_string.append(key[i])
            try_num += 1
    return key_string


# Decodes the code to it's true numeric value
def encode(code, key):
    encoded_numeric_array = []
    code_len = len(code)

    for i in range(0, code_len, 1):
        encoded_value = code[i] + key[i]
        if encoded_value >= len(alphabetic_array):
            encoded_value -= 26
            encoded_numeric_array.append(encoded_value)
        else:
            encoded_numeric_array.append(encoded_value)
    return encoded_numeric_array


# Converts the decoded code to it's alphabetic value
def convert_to_alphabet(code):
    code_len = len(code)
    decoded_alphabet = []
    for i in range(0, code_len, 1):
        alphabetic_number = alphabetic_array[code[i]]  # The index of the alphabetic array to be called
        decoded_alphabet.append(alphabetic_number)
    return decoded_alphabet


def get_input():
    (code_array, code_len) = get_code_array()
    key_array = get_key_array()
    return code_array, key_array, code_len


def convert_to_numeric(code, key):
    numerated_code = numerate(code)  # array of numeric code values
    numerated_key = numerate(key)
    return numerated_code, numerated_key


# Converts the plain_text array to a string
def print_result(result_array):
    result_len = len(result_array)
    result_string = ""
    for i in range(0, result_len, 1):
        result_string = result_string + result_array[i]
    print(result_string)


(code_array, key_array, code_len) = get_input()  # Gets the code and the key from user
key_string = generate_key(key_array, code_len)  # Generates an array with the key repeating for the length of the code
(numerated_code, numerated_key) = convert_to_numeric(code_array, key_string)
encoded_value = encode(numerated_code, numerated_key)  # Returns the decoded numeric values in an array
encoded_text_array = convert_to_alphabet(encoded_value)  # Converts

print_result(encoded_text_array)

