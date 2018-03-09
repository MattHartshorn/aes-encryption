import os
import random

seeded = False

def generate(size=256):
    """ Randomly generates an array of bytes used for AES encryption

    Arguments:
    size -- The size of the key to generate, number of bits (default: 256)

    Returns:
    Randomly generated key as byte array

    Raises:
    Exception -- The key size must be 128, 192, or 256
    """

    if (size != 128 and size != 192 and size != 256): 
        raise Exception("Invalid size, key size must be 128, 192, or 256 bits")

    size = int(size / 8)

    try:
        return os.urandom(size)
    except NotImplementedError:
        if (not seeded): seed()
        return bytes([random.randint(0, 255) for i in range(0, size)])


def seed(seed = None):
    """ Seeds the random number generator

    Arguments:
    seed -- value to see the generator with 
    """
    if (seed == None): random.seed()
    else: random.seed(seed)
    
    seeded = True