from PIL import Image
import stepic

# The example image used is named edelweiss.png
class bookCipher:
    def __init__(self, book):
        with open(book, 'r') as book_doc:
            self.book_to_encode = book_doc.read().lower().split()

    def encrypt(self, message):
        encryption = ''
        words = message.lower().split()
        for word in words:
            try:
                word_index = self.book_to_encode.index(word)
                encryption += str(word_index) + ' '
            except:
                print(f"('{word}' not in text)")
                for letter in words:
                        encryption += "* "

        return encryption

    def decrypt(self, encrypted):
        decrypted = ''
        code = encrypted.split()
        for number in code:
            if number == ' ':
                decrypted += ' '
            else:
                try:
                    int(number) == self.book_to_encode[int(number)]
                    decrypted += self.book_to_encode[int(number)] + ' '
                except:
                    print(f"('{number}' not in text)")
                    decrypted += number + ' '

        return decrypted

class steganography:
    def __init__(self, image):
        self.image = image

    def steg_encrypt(self, message):
        message = message.encode()
        encoded_img = stepic.encode(self.image, message)
        encoded_img.save("edelweiss.png")
        self.image = Image.open("edelweiss.png")

    def steg_decrypt(self):
        decoded_msg = stepic.decode(self.image)
        return decoded_msg



book = # Add txt file link here for cipher

book_cipher_key = bookCipher(book)
message = input("Enter message to encrypt: ")

encrypted = book_cipher_key.encrypt(message)
print(f"encrypted text: {encrypted}")
decrypted = book_cipher_key.decrypt(encrypted)
print(f"decrypted text: {decrypted}")

image = Image.open("edelweiss.png")
clue = # Add clue as a string (optional)

steg = steganography(image)
steg.steg_encrypt(encrypted)
print(f"{clue + ': ' + steg.steg_decrypt()}")