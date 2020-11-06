#!/usr/env/bin python3

####################
# Vigenere Encoder v1.3.
# Made by TeknoBen96
# 11/6/2020
####################


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
    "A",    # 26
    "B",    # 27
    "C",    # 28
    "D",    # 29
    "E",    # 30
    "F",    # 31
    "H",    # 32
    "I",    # 33
    "J",    # 34
    "K",    # 35
    "L",    # 36
    "M",    # 37
    "N",    # 38
    "O",    # 39
    "P",    # 40
    "Q",    # 41
    "R",    # 42
    "S",    # 43
    "T",    # 44
    "U",    # 45
    "V",    # 46
    "W",    # 47
    "X",    # 48
    "Y",    # 49
    "Z",    # 50
    " ",    # 51
    ",",    # 52
    ".",    # 53
    "?",    # 54
    "!",    # 55
    "'",    # 56
    "\""    # 57
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
    "z": 25,
    "A": 26,
    "B": 27,
    "C": 28,
    "D": 29,
    "E": 30,
    "F": 31,
    "H": 32,
    "I": 33,
    "J": 34,
    "K": 35,
    "L": 36,
    "M": 37,
    "N": 38,
    "O": 39,
    "P": 40,
    "Q": 41,
    "R": 42,
    "S": 43,
    "T": 44,
    "U": 45,
    "V": 46,
    "W": 47,
    "X": 48,
    "Y": 49,
    "Z": 50,
    " ": 51,
    ",": 52,
    ".": 53,
    "?": 54,
    "!": 55,
    "'": 56,
    "\"": 57
    }

alphabetic_array_len = len(alphabetic_array)

# Makes and returns an array with the code characters
def get_text_array():
    text = input("[+] Enter text here >>> ")
    text_len = len(text)
    text_array = []
    for i in range(0, text_len, 1):
        text_array.append(text[i])
    return text_array, text_len


# Makes and returns an array with the key characters
def get_key_array():
    key = input("[+] Enter encryption key >>> ")
    key_array = []
    for i in range(0, len(key), 1):
        key_array.append(key[i])
    return key_array


def get_input():
    (text_array, text_len) = get_text_array()
    key_array = get_key_array()
    return text_array, key_array, text_len

# Converts code in to numeric values and returns then in an array
def numerate(code):
    numerated_array = []
    code_len = len(code)
    for i in range(0, code_len, 1):
        numerated_array.append(char_num[code[i]])
    return numerated_array


# Generates a repeating key for the length of the code, then returns it as an array
def generate_key(key, code_len):
    key_array = key
    for i in range(0, code_len, 1):
        key_array.append(key[i])
    return key_array


# Decodes the code to it's true numeric value
def encode(text, key):
    encoded_numeric_array = []
    for i in range(0, len(text), 1):
        encoded_value = text[i] + key[i]
        if encoded_value >= alphabetic_array_len:
            encoded_value -= alphabetic_array_len
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
    print("[+] Encoded to >>> " + result_string)


(text_array, key_array, text_len) = get_input()  # Gets the code and the key from user
key_string = generate_key(key_array, text_len)  # Generates an array with the key repeating for the length of the code
(numerated_text, numerated_key) = convert_to_numeric(text_array, key_string)
encoded_value = encode(numerated_text, numerated_key)  # Returns the decoded numeric values in an array
encoded_text_array = convert_to_alphabet(encoded_value)  # Converts encoded numeric text array to alphabetic values

print_result(encoded_text_array)

