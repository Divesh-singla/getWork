import hashlib
def __encryptorMD5(password):
    encrypted = hashlib.md5(password.encode())

    return(encrypted.hexdigest())