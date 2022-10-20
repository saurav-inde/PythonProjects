import hashlib

def sha_512(string:str):
    encoded_string = string.encode()
    hash = hashlib.sha512(encoded_string)
    return str(hash.hexdigest())



