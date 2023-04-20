#jasmin ericka celebre
#problem 3 the vigenere cipher

import pyfiglet 
#ask user for message and key then save it
message = input("Please type the message(all uppercase letters, no spaces): ").strip()
key = input("Please type the key (all uppercase letters): ")
if message.islower() | key.islower() == True:
    print("The message or key that you enter contains lowercase letters. Please follow the instructions.")
else:
# convert the key to numbers
    num_key = [ord(char) - ord('A') for char in key]
# convert the plaintext to numbers
    num_message = [ord(char) - ord('A') for char in message]
# encrypt the message
    ciphertext = ''
    for i in range(len(message)):
#addition and modulus computation
        ciphertext += chr((num_message[i] + num_key[i % len(key)]) % 26 + ord('A'))
# print the output
    print("=*"*80)
    print("MESSAGE:")
    print(pyfiglet.figlet_format(message, font="smkeyboard", justify="center"))
    print("KEY:")
    print(pyfiglet.figlet_format(key, font="smkeyboard", justify="center"))
    print("Vigenere Ciphertext:")
    print("=*"*80)