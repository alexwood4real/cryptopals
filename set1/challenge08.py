#######################################################################################################################
##### SET 1, CHALLENGE 8 ##############################################################################################
##### https://cryptopals.com/sets/1/challenges/8 ######################################################################

### Imports
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from utils.file_io import read_input_lines, write_output

def set_1_challenge_8():
    # read the individual strings as a list
    msg_list = read_input_lines("challenge_8.txt")
    output = ""

    # iterate through the list of hex encoded strings
    for msg_idx, msg in enumerate(msg_list):
        msg_bytes = bytes.fromhex(msg)

        # split each line into 16 blocks
        blocks = [
            msg_bytes[i:i + 16]
            for i in range(0, len(msg_bytes), 16)
        ]

        # if any duplicate blocks exist, that line is ecrypted in ECB mode
        if len(blocks) != len(set(blocks)):
            output += f"The line that is encrypted in ECB mode is line {msg_idx} with the text:\n{str(msg_list[msg_idx])}"

    write_output("challenge_8_output.txt", output)