#######################################################################################################################
##### SET 1, CHALLENGE 3 ##############################################################################################
##### https://cryptopals.com/sets/1/challenges/3 ######################################################################

### Imports
from utils.xor import break_single_byte_xor

# C = P XOR K, s.t.
# C := Cypher text
# P := Plaintext byte
# K := single-byte key
# 256 ascii characters; therefore, 256 possible keys
def set_1_challenge_3(hex_str):
    result = break_single_byte_xor(hex_str)

    # get the highest score and decrypt
    score, key, text = result[0]

    print(f"Score: {score:.4f}")
    print(f"Key: {key} ({chr(key) if 32 <= key <= 126 else "nonprintable"})")
    print(f"Plaintext: {text.decode("ascii")}")
