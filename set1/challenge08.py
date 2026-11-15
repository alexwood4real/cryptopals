#######################################################################################################################
##### SET 1, CHALLENGE 8 ##############################################################################################
##### https://cryptopals.com/sets/1/challenges/8 ######################################################################

### Imports
from utils.ecb import is_aes_ecb
from utils.file_io import read_input_lines, write_output

def set_1_challenge_8():
    # read the individual strings as a list
    msg_list = read_input_lines("challenge_8.txt")
    output = ""

    # iterate through the list of hex encoded strings
    for msg_idx, msg in enumerate(msg_list):
        msg_bytes = bytes.fromhex(msg)

        if is_aes_ecb(msg_bytes):
            output += f"The line that is encrypted in ECB mode is line {msg_idx} with the text:\n{str(msg_list[msg_idx])}"

    write_output("challenge_8_output.txt", output)