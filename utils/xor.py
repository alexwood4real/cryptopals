### Imports
from utils.scoring import score_txt

### Functions

# performs XOR on two fixed hexadecimal integers
def hex_xor(a, b):
    dec_a = int(a, 16)
    dec_b = int(b, 16)
    xor_val = dec_a ^ dec_b
    return str(hex(xor_val))

# performs a XOR on every byte in a text with a single key
def single_byte_xor(cipher, key):
    return bytes( byte ^ key for byte in cipher)

# performs XOR for every ascii key and return scores
def break_single_byte_xor(hex_str):
    cipher_txt = bytes.fromhex(hex_str)

    candidates = []

    # iterate through all ascii codes
    for key in range(256):
        text = single_byte_xor(cipher_txt, key)
        score = score_txt(text)

        candidates.append((score, key, text))

    candidates.sort(reverse=True)

    # return list of candidates is descending score order
    return candidates