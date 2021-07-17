def read(path):
    with open(path, "r") as f:
        return f.read()


class VigenereCoder:
    def __init__(self, input_str, key):
        self.charset_file = "charset.txt"
        self.charset = list(read(self.charset_file))
        self.max_index = len(self.charset) - 1
        self.key_char_index = 0
        self.key = key
        self.key_len = len(key)
        self.input_str = input_str
        self.output_str = ""

    def update_key_char(self):
        self.key_char_index += 1
        if self.key_char_index >= self.key_len:
            self.key_char_index = 0

    def get_char_num_values(self, char):
        key_char = self.key[self.key_char_index]
        return self.charset.index(char), self.charset.index(key_char)


class Encoder(VigenereCoder):
    def encode_char(self, char):
        char_num_value, key_num_value = self.get_char_num_values(char)
        encoded_value = char_num_value + key_num_value
        if encoded_value >= self.max_index:
            encoded_value -= self.max_index

        self.update_key_char()
        return self.charset[encoded_value]

    def run(self):
        for char in self.input_str:
            encoded_char = self.encode_char(char)
            self.output_str += encoded_char
        return self.output_str


class Decoder(VigenereCoder):
    def decode_char(self, char):
        char_num_value, key_num_value = self.get_char_num_values(char)
        decoded_value = char_num_value - key_num_value
        if decoded_value < 0:
            decoded_value += self.max_index

        self.update_key_char()
        return self.charset[decoded_value]

    def run(self):
        for char in self.input_str:
            decoded_char = self.decode_char(char)
            self.output_str += decoded_char
        return self.output_str
