#######################################################################################################################
##### SET 1, CHALLENGE 3 ##############################################################################################
##### https://cryptopals.com/sets/1/challenges/3 ######################################################################

### Imports
from utils.xor import break_single_byte_xor
from utils.file_io import read_input, write_output

# C = P XOR K, s.t.
# C := Cypher text
# P := Plaintext byte
# K := single-byte key
# 256 ascii characters; therefore, 256 possible keys
def set_1_challenge_3():
    hex_str = read_input("challenge_3.txt")
    result = break_single_byte_xor(hex_str)

    # get the highest score and decrypt
    score, key, text = result[0]

    output = (
        f"Score: {score:.4f}\n"
        f"Key: {key} ({chr(key)})\n"
        f"Plaintext: {text.decode("ascii")}"
    )
    write_output("challenge_3_output.txt", output)