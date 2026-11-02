### Imports
import base64
from utils.xor import hex_xor

### Constants
# Alphabet
alphabet_lib = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

### Functions
# decodes a hex string
def decode_hex_string(hex_str):
    i = 0
    while i < 26:
        res = hex_xor(hex_str, alphabet_lib[i].encode("utf-8").hex())
        print(res)
        print(i)
        print(res.decode("hex"))
        i += 1

# returns hex string to base64 string
def hex_to_64(num):
    raw_bytes = bytes.fromhex(num)
    encoded = base64.b64encode(raw_bytes)
    return encoded.decode("ascii")