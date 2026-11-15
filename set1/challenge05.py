#######################################################################################################################
##### SET 1, CHALLENGE 5 ##############################################################################################
##### https://cryptopals.com/sets/1/challenges/5 ######################################################################

### Imports
from utils.file_io import read_input_raw, write_output
from utils.xor import repeating_key_byte_xor

def set_1_challenge_5():
    key = "ICE"
    text = read_input_raw("challenge_5.txt").encode("utf-8")

    encrypt = repeating_key_byte_xor(text, key)
    write_output("challenge_5_output.txt", encrypt.hex())