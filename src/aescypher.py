from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

BLOCK_SIZE = 16

def encrypt(plaintext, key, mode="ECB", iv=None):
    cipher = getCipher(key, mode, iv, True)
    plaintext = addPadding(plaintext)
    return cipher.encryptor().update(plaintext)

def decrypt(cyphertext, key, mode="ECB", iv=None):
    cipher = getCipher(key, mode, iv, False)
    plaintext = cipher.decryptor().update(cyphertext)
    return removePadding(plaintext)

def getCipher(key, mode_str, iv, isEncrypt):
    algorithm = algorithms.AES(key)

    mode = None
    if (mode_str.upper() == "ECB"):
        mode = modes.ECB()
    elif (mode_str.upper() == "CBC"):
        mode = modes.CBC(iv)
    else:
        raise ValueError("Invalid mode, please specify 'ECB' or 'CBC'")

    return Cipher(algorithm, mode, default_backend())

def addPadding(data):
    if (len(data) == 0):
        data = bytes([BLOCK_SIZE] * BLOCK_SIZE)
    elif (len(data) % BLOCK_SIZE != 0):
        padding = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
        data = bytearray(data)
        data.extend(bytes([padding] * padding))
        data = bytes(data)
    
    return data

def removePadding(data):
    if (len(data) == 0 or len(data) % BLOCK_SIZE != 0):
        raise ValueError("Invalid message size")

    padding = data[-1]
    start = len(data) - padding
    for byte in data[start:]:
        if (byte != padding): return data

    return data[:start]
