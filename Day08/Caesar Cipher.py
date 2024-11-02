from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")

def decrypt(original_text, shift_amount):
    output_text = ""
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) - shift_amount
            output_text += alphabet[shifted_position]
    print(f"Here is the decrypted result: {output_text}")

def caesear():
    if direction == 'encode':
        encrypt(original_text=text, shift_amount=shift)
    elif direction == 'decode':
        decrypt(original_text=text, shift_amount=shift)
    else:
        print("Please only print in encode or decode.")

caesear()

restart = input("Type yes if you want to go again. Otherwise, type no to exit.\n").lower()

while restart == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesear()
    restart = input("Type yes if you want to go again. Otherwise, type no to exit.\n").lower()
else:
    print("Goodbye, see you again.")


