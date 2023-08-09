alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
encoded_text = []
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text,shift_amount):
  for letter in plain_text:
    position = (alphabet.index(letter) + shift_amount ) % 26
    #solution 2
    # position = 26 - alphabet.index(letter)
    # shifted_position = shift - position
    encoded_text.append(alphabet[position])
  cipher_text = ("".join(encoded_text))
  print(f"The encoded text is {cipher_text}")

def decrypt(encoded_message,shift_amount):
  for letter in encoded_message:
    position = (alphabet.index(letter) - shift_amount ) % 26
    #solution 2
    # position = 26 - alphabet.index(letter)
    # shifted_position = shift - position
    encoded_text.append(alphabet[position])
  cipher_text = ("".join(encoded_text))
  print(f"You decoded text is {cipher_text}")
    
  
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
if direction == "encode":
  encrypt(plain_text=text,shift_amount=shift)
elif direction == "decode":
  decrypt(encoded_message=text,shift_amount=shift)