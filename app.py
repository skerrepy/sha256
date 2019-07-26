import hashlib
"""
Author:Omar hanafi
"""
class encrypt:
    def __init__(self,hash_string):
        self.hash_string = hash_string
    def letsEncrypt(self):
        sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
        return sha_signature
hash_string = input("msg to encrypt ?")

print(encrypt.letsEncrypt(hash_string))
