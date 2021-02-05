#!/usr/env/bin python3

####################
# Vigenere Encoder v1.3.
# Made by TeknoBen96
# 11/6/2020
####################

charset_path = "charset.txt"

def read_file(path):
    with open(path, "rb") as file:
        content = file.read().decode()  # needs to be decoded in Python3
    return content


def create_charset(charset_path):
    charset_array = []
    content = read_file(charset_path)
    for i in range(0, len(content), 1):
        if not content[i] in charset_array and not content[i] == "\n":
            charset_array.append(content[i])
    return charset_array


charset = create_charset(charset_path)
charset_len = len(charset)
print(charset)

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
        print(charset.index(code[i]))
        numerated_array.append(charset.index(code[i]))
    return numerated_array


# Generates a repeating key for the length of the code, then returns it as an array
def generate_key(key, code_len):
    key_array = key
    for i in range(0, code_len, 1):
        key_array.append(key[i])
    return key_array


# Encodes the code to it's true numeric value
def encode(text, key):
    encoded_numeric_array = []
    for i in range(0, len(text), 1):
        encoded_value = text[i] + key[i]
        if encoded_value >= charset_len:
            encoded_value -= charset_len
            encoded_numeric_array.append(encoded_value)
        else:
            encoded_numeric_array.append(encoded_value)
    return encoded_numeric_array


# Converts the encoded code to it's alphabetic value
def convert_to_alphabet(code):
    code_len = len(code)
    decoded_alphabet = []
    for i in range(0, code_len, 1):
        alphabetic_number = charset[code[i]]
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
    print("[+] Encoded to -->" + result_string + "<--")


(text_array, key_array, text_len) = get_input()  # Gets the code and the key from user
key_string = generate_key(key_array, text_len)  # Generates an array with the key repeating for the length of the code
(numerated_text, numerated_key) = convert_to_numeric(text_array, key_string)
encoded_value = encode(numerated_text, numerated_key)  # Returns the decoded numeric values in an array
encoded_text_array = convert_to_alphabet(encoded_value)  # Converts encoded numeric text array to alphabetic values

print_result(encoded_text_array)
