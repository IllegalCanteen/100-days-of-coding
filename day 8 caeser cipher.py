alphabets = list("abcdefghijklmnopqrstuvwxyz0123456789 .,!?$%/()*-@#^&_'\"=:;[]{}~+`")
from caeser_cypher_logo import logo
print(logo)
def encrypt():
   encrypted_word=""
   original_text = input("What message do you want to encrypt: ").lower()
   shift_amount = int(input("How many letters do you want to shift your message by? "))
   for letters in original_text:
       original_position = alphabets.index(letters)
       new_position = (original_position + shift_amount) % len(alphabets)
       new_letter = alphabets[new_position]
       encrypted_word = encrypted_word + new_letter
   print(f"Your encrypted message is: {encrypted_word}")


def decrypt():
    decrypted_word=""
    encrypted_text = input("What message do you want to decrypt: ").lower()
    shift_amount = int(input("How many letters do you want to shift your message back  by? "))
    for letters in encrypted_text:
        letter_position = alphabets.index(letters)
        re_position = (letter_position - shift_amount) % len(alphabets)
        decrypted_word = decrypted_word + alphabets[re_position]
    print(f"Your decrypted message is: {decrypted_word}")

response=input("Do you want to encrypt(e) or decrypt(d): ").lower()
def caeser(response):
    if response == "e":
        encrypt()
    elif response == "d":
        decrypt()
    else:
        print("Invalid response")
caeser(response)
