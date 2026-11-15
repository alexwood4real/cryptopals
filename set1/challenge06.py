#######################################################################################################################
##### SET 1, CHALLENGE 6 ##############################################################################################
##### https://cryptopals.com/sets/1/challenges/6 ######################################################################

### Imports
import base64
from utils.file_io import read_input_raw, write_output
from utils.common import break_single_byte_xor, calc_key_len, transpose_msg
from utils.xor import repeating_key_byte_xor

### Constants

# Challenge 6 output directory
CHALLENGE_6_OUTPUTS = "challenge_6_outputs"

def set_1_challenge_6():
    msg = base64.b64decode(read_input_raw("challenge_6.txt"))

    # find list of potential key sizes
    key_sizes = calc_key_len(msg)

    # transpose the blocks for the respective keysizes
    block_list = transpose_msg(msg, key_sizes)

    # perform break_single_byte_xor on each block idx
    key_list = []
    for key_it, key_size in enumerate(key_sizes):    
        key = ""
        # solve for that key
        for l_it in range(key_size):
            l_list = block_list[key_it][l_it]
            l = break_single_byte_xor(l_list)
            key += chr(l[0][1])
        key_list.append(key)

    # perform repeating_key_byte_xor for each key
    for idx, key in enumerate(key_list):
        result = repeating_key_byte_xor(msg, key).decode("utf-8")
        output_str = CHALLENGE_6_OUTPUTS + "/challeng_6_output_" + str(idx) + ".txt"
        write_output(output_str, result)
