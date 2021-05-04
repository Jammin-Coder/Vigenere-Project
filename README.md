# vigenere-project


You are alowed to copy and use my code freely, without any restrictions... atribution wouldn't hurt though :)

This is a simple project that allows you to decode and encode text with the Vigenere Cipher.  

To use it, just run the decoder or encoder python file  
in a Python 3 interpreter.  

The encoder encodes plain text with a given key.  
The decoder decoded ciphered text with a given key.  

NOTE: All characters are case sensitive: "a" holds a differant value than "A".  

I.E  

Encoder  
```
[+] Enter text here >>> Hey! What's up!?
[+] Enter encryption key >>> cat
[+] Encrypted to >>> JeS" ijaNasmwpq
```
  
Decoder  
```
[+] Enter code here >>> JeS" ijaNasmwpq
[+] Enter key >>> cat
[+] Decoded to >>> Hey! What's up!?
```

It is possible for spaces to be ANYWHERE in the encrypted text, 
even invisible at the end of the line. So be sure to copy the full line of encrypted text when decoding.  
