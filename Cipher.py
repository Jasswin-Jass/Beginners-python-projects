alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def coder(original_text, shift_amount, encode_or_decode) :
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for l in original_text:

        if l not in alphabets:
            output_text += l
            continue
        
        shifted_position = alphabets.index(l) + shift_amount
        shifted_position %= len(alphabets)
        output_text += alphabets[shifted_position]
    return output_text

while(1):

    direction = input("Type 'encode' to encrypt and 'decode' to decrypt: ").lower()

    if direction == 'encode' or direction == "decode":

        text = input("Type your message: ").lower()
        shift = int(input("Type the shift number: "))
        cipherText = coder(original_text=text, shift_amount=shift, encode_or_decode=direction)
        print(f"Here is the encoded text: {cipherText}")

    else:
        print("Invalid choice")

    go = input("If you want to go again type 'yes' otherwise type 'no' ").lower()
    if go == "yes":
        continue
    else :
        break
    
print('Done')