import hashlib
from Crypto.Cipher import AES
from Crypto import Random
from base64 import  b64encode, b64decode


AES_KEY = "+KbPeShVkYp3s6v9"
AES_IV = "6v9y$B&E)H@McQfT"


class AESCipher(object):

    def __init__(self, key):
        # AES Block Size of 16 Bit;;
        self.block_size = AES.block_size
        # Key Generation with hashlib;;
        self.key = hashlib.sha256(key.encode('utf-8')).digest()

    def encrypt(self, plain_text):
        # First we pad that plain_text in order to be able to encrypt it
        plain_text = self.__pad(plain_text)
        print(f"plain_text: {plain_text}")
        # Generate a new random iv with the size of an AES block, 128bits
        iv = Random.new().read(self.block_size)
        # We now have to create our AES cipher with AES.new with our key,
        # in mode CBC and with our just generated iv.
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        # we now invoke the encrypt function of our cipher, passing it
        # our plain_text converted to bits
        encrypted_text = cipher.encrypt(plain_text.encode())
        return b64encode(iv + encrypted_text).decode("utf-8")

    def decrypt(self, encrypted_text):
        encrypted_text = b64decode(encrypted_text)
        iv = encrypted_text[:self.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plain_text = cipher.decrypt(encrypted_text[self.block_size:]).decode("utf-8")
        return self.__unpad(plain_text)

    @staticmethod
    def __pad(self, plain_text):
        # adds a numbers bytes for the text to be a multiple of 128 bits
        number_of_bytes_to_pad = self.block_size - len(data) % self.block_size
        print(f"number_of_bytes_to_pad: {number_of_bytes_to_pad}")
        # number is stored in number_of_bytes_to_pad and
        # in ascii_stringwe generate our padding character
        ascii_string = chr(number_of_bytes_to_pad)
        print(f"ascii_string: {ascii_string}")
        # padding_str will contain that character times number_of_bytes_to_pad
        padding_str = number_of_bytes_to_pad * ascii_string
        print(f"padding_str: {padding_str}")
        # now we've to add padding_str at the end of our plain_text so
        # that it is now a multiple of 128 bits.
        padded_plain_text = plain_text + padding_str
        return padded_plain_text

    @staticmethod
    def __unpad(self, plain_text):
        # __unpadmethod will receive the decrypted text, also known as plain_text
        # and will remove all the extra added characters in the __pad
        last_character = plain_text[len(plain_text) - 1:]
        # we first must identify the last character and store in bytes_to_remove
        # how many bytes we need to trim of the end of plain_text in order to unpad it.
        bytes_to_remove = ord(last_character)
        return plain_text[:-bytes_to_remove]


def main():
    mobile_no = '12345678̐0'
    resp = AESCipher().encrypt(mobile_no)
    print(f"Encrypted Data: {resp}")


if __name__ == "__main__":
    main()