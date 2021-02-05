#!/usr/env/bin python3

########################
# Vigenere Decoder v1.3.
# Made by TeknoBen96
# 11/6/2020
#########################

# This array stores letters to be called during deciphering


def read(path):
    with open(path, "rb") as file:
        content = file.read().decode()  # needs to be decoded in Python3
    return content


def create_charset(charset_path):
    charset_array = []
    content = read(charset_path)
    for i in range(0, len(content), 1):
        if not content[i] in charset_array and not content[i] == "\n":
            charset_array.append(content[i])
    return charset_array


charset_path = "charset.txt"
charset = create_charset(charset_path)
charset_len = len(charset)

# Makes and returns an array with the code characters
def get_code_array():
    code = input("[+] Enter code here >>> ")
    code_len = len(code)
    code_array = []
    for i in range(0, code_len, 1):
        code_array.append(code[i])
    return code_array, code_len


# Makes and returns an array with the key characters
def get_key_array():
    key = input("[+] Enter decryption key >>> ")
    key_len = len(key)
    key_array = []
    for i in range(0, key_len, 1):
        key_array.append(key[i])
    return key_array


def get_input():
    (code_array, code_len) = get_code_array()
    key_array = get_key_array()
    return code_array, key_array, code_len


# Converts code in to numeric values and returns then in an array
def numerate(code):
    numerated_array = []
    code_len = len(code)
    for i in range(0, code_len, 1):
        numerated_array.append(charset.index(code[i]))
    return numerated_array


# Generates a repeating key for the length of the code, then returns it as an array
def generate_key(key, code_len):
    key_string = key
    for i in range(0, code_len, 1):
        key_string_len = len(key_string)
        if key_string_len < code_len:
            key_string.append(key[i])
    return key_string


# Decodes the code to it's true numeric value
def decode(code, key):
    decoded_numeric_array = []
    code_len = len(code)
    for i in range(0, code_len, 1):
        decoded_value = code[i] - key[i]
        decoded_numeric_array.append(decoded_value)
    return decoded_numeric_array


# Converts the decoded code to it's alphabetic value
def convert_to_alphabet(code):
    code_len = len(code)
    decoded_alphabet = []
    for i in range(0, code_len, 1):
        alphabetic_number = charset[code[i]]  # The index of the alphabetic array to be called
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
    print("[+] Decoded to -->" + result_string + "<--")


(code_array, key_array, code_len) = get_input()  # Gets the code and the key from user
key_string = generate_key(key_array, code_len)  # Generates an array with the key repeating for the length of the code
(numerated_code, numerated_key) = convert_to_numeric(code_array, key_string)
decoded_value = decode(numerated_code, numerated_key)  # Returns the decoded numeric values in an array
plain_text_array = convert_to_alphabet(decoded_value)  # Converts

print_result(plain_text_array)
