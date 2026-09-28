import random
KEY = random.randint(1, 255)
plaintext = b"part3:???????????"
ct = bytes(b ^ KEY for b in plaintext)
print(ct.hex())

# output: 2a3b282e6960382f31632f35382c38693e3523
# Throw KtTJPt9B in the bin and find me on 275
