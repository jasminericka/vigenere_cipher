#jasmin ericka celebre
#problem 3 the vigenere cipher

#ask user for message and key then save it
message = input("Please type the message(all uppercase letters, no spaces): ").strip()
key = input("Please type the key (all uppercase letters): ")
if message.islower() | key.islower() == True:
    print("The message or key that you enter contains lowercase letters. Please follow the instructions.")
else:
# convert the key to numbers
    num_key = [ord(char) - ord('A') for char in key]
# convert the plaintext to numbers
# encrypt the message
#addition and modulus computation
# print the output