from Crypto import Random
from Crypto.Cipher import AES

# key = b'\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18'
key = 'A56559C3FAD8612695AA4278CE991BA9'

class Crypto:

    @staticmethod
    def pad(s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    @staticmethod
    def encrypt(message):
        message = Crypto.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)

    @staticmethod
    def decrypt(ciphertext):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")

    @staticmethod
    def encrypt_file(file_name, extension):
        with open(file_name + extension, 'rb') as SelectedFile:
            plaintext = SelectedFile.read()
        enc = Crypto.encrypt(plaintext)
        with open("EncryptedFile.enc", 'wb') as EncryptedFile:
            EncryptedFile.write(enc)

    @staticmethod
    def decrypt_file(file_name, extension):
        with open(file_name + extension, 'rb') as EncryptedFile:
            ciphertext = EncryptedFile.read()
        dec = Crypto.decrypt(ciphertext)
        with open("DecryptedFile.txt", 'wb') as DecryptedFile:
            DecryptedFile.write(dec)
