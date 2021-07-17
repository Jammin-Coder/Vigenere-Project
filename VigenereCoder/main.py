from VigenereCoder.Coder import *


MODE = input("Encode or decode? [e/d]").lower()

if MODE == "e":
  text = input("Enter text >> ")
  key = input("Enter key >> ")
  output = Encoder(text, key).run()
  print(output)

elif MODE == "d":
  code = input("Enter code >> ")
  key = input("Enter key >> ")
  output = Decoder(code, key).run()
  print(output)
