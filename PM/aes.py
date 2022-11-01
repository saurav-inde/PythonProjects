import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES


class AESCipher(object):

    def __init__(self, key):
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw.encode()))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s) - 1:])]


key = input("enter the key: ")
encrypted_data = b'CL91hhrVJaySuVeMI4d7vdm7Wo6EXcnuqXWX1mndwED57N50Q29DXq+EtYPen9z8lcKzGYZhCkR8dng4EaxLdHavvzWu3kx7jXCOrdVboDJMzahF7GjPMf14GXiBpJ/lSm3ncFpY2gxAfcK5lPfsWQ=='
# raw = input("enter the data to be encrypted: ")
encrypted = AESCipher(key)
# encrypted_data =encrypted.encrypt(raw)

print(encrypted_data)
print("\n")
print(encrypted.decrypt(encrypted_data))
