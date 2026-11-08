#######################################################################################################################
##### SET 1, CHALLENGE 5 ##############################################################################################
##### https://cryptopals.com/sets/1/challenges/51 ######################################################################

### Imports
from utils.file_io import read_input_lines, write_output
from utils.xor import repeating_key_byte_xor

def set_1_challenge_5():
    key = "ICE"
    text = read_input_lines("challenge_5.txt")

    encrypt = repeating_key_byte_xor(text, key)
    write_output("challenge_5_output.txt", encrypt)