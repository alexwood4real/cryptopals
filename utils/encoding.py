### Imports
import base64
from utils.xor import hex_xor

### Constants

# Base 64 map
base_64_dict = { 0: "A",  1: "B",  2: "C",  3: "D",  4: "E",  5: "F",  6: "G",  7: "H", 
                 8: "I",  9: "J", 10: "K", 11: "L", 12: "M", 13: "N", 14: "O", 15: "P", 
                16: "Q", 17: "R", 18: "S", 19: "T", 20: "U", 21: "V", 22: "W", 23: "X", 
                24: "Y", 25: "Z", 26: "a", 27: "b", 28: "c", 29: "d", 30: "e", 31: "f", 
                32: "g", 33: "h", 34: "i", 35: "j", 36: "k", 37: "l", 38: "m", 39: "n", 
                40: "o", 41: "p", 42: "q", 43: "r", 44: "s", 45: "t", 46: "u", 47: "v", 
                48: "w", 49: "x", 50: "y", 51: "z", 52: "0", 53: "1", 54: "2", 55: "3",
                56: "4", 57: "5", 58: "6", 59: "7", 60: "8", 61: "9", 62: "+", 63: "/"}

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

# The modified Euclidean Algorithm to change bases
# num = q * base + r
def mod_ea_base_convert(num, base, p):
    q = num // pow(base, p)
    r = num % pow(base, p)
    if p == 0:
        return base_64_dict[q]
    else:
        return base_64_dict[q] + mod_ea_base_convert(r, base, p-1)

# finds starting exponent for modified EA
def find_closest_exp(base, num):
    i = 0
    while pow(base, i) < num:
        i += 1
    if i == 0:
        return i
    else:
        return i - 1

# returns hex string to base64 string
def hex_to_64(num):
    num_b10 = int(num, 16)
    power = find_closest_exp(64, num_b10)
    num_b64 = mod_ea_base_convert(num_b10, 64, power)
    return num_b64