#######################################################################################################################
##### SET 2, CHALLENGE 10 #############################################################################################
##### https://cryptopals.com/sets/2/challenges/10 #####################################################################

### Imports
import base64
from utils.blocks import decrypt_aes_128_cbc
from utils.file_io import read_input_raw, write_output

### Constants

# Challenge 10 output directory
CHALLENGE_10_OUTPUTS = "challenge_10_outputs/"

# Plan:
# Given a following text in base 64
# 1. decrypt in CBC the easy way
# 2. verify be encrypting in CBC the easy way
# 3. do steps 1 & 2 the long way (using xor) 
# 4. write to a challenge 10 output directory for each method
def set_2_challenge_10():
    # set up key, message, and initialization vector
    key = b"YELLOW SUBMARINE"
    msg = base64.b64decode(read_input_raw("challenge_10.txt"))
    iv = b"\x00" * 16

    # 1. decrypt in CBC the easy way
    decrypt_cbc_easy = decrypt_aes_128_cbc(key, msg, iv)
    output_path = CHALLENGE_10_OUTPUTS + "decrypt_cbc_easy.txt"
    write_output(output_path, decrypt_cbc_easy.decode("utf-8"))

    