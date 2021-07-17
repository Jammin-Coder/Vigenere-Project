from VigenereCoder.Coder import *


text = "this is a test"
key = "apples and oranges"

encoded_text = Encoder(text, key).run()
decoded_text = Decoder(encoded_text, key).run()

print(encoded_text)
print(decoded_text)
