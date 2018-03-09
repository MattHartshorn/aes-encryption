import time
import sys
import aescypher
import keygenerator

plaintext = "Welcome to data security and privacy ."
b_plaintext = plaintext.encode()
key = keygenerator.generate()

mode =  "CBC"
iterations = 100000

print("Info")
print("-------------------------")
print("Plaintext: {0}".format(plaintext))
print("Key: {0}".format(key.hex()))
print("")


# Measure encryption timing
start = time.time()
for i in range(iterations):
    iv = keygenerator.generate(128)
    aescypher.encrypt(b_plaintext, key, mode, iv)
end = time.time()
elapsed = (end - start) * 1000

print("Encryption")
print("-------------------------")
print("Start: {0}".format(start))
print("End: {0}".format(end))
print("Elapsed: {0:.4f} ms".format(elapsed))
print("Avergae: {0:.4f} ms".format(elapsed / iterations))
print("")

# Generate cyphertext
iv = keygenerator.generate(128)
ct = aescypher.encrypt(b_plaintext, key, mode, iv)

# Measure decryption timing
start = time.time()
for i in range(iterations):
    aescypher.decrypt(ct, key, mode, iv)
end = time.time()
elapsed = (end - start) * 1000

print("Decryption")
print("-------------------------")
print("IV: {0}".format(iv.hex()))
print("Start: {0}".format(start))
print("End: {0}".format(end))
print("Elapsed: {0:.4f} ms".format(elapsed))
print("Average: {0:.4f} ms".format(elapsed / iterations))


