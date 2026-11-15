#######################################################################################################################
##### SET 2, CHALLENGE 9 ##############################################################################################
##### https://cryptopals.com/sets/2/challenges/9 ######################################################################

### Imports
from utils.ecb import pkcs7_pad
from utils.file_io import write_output

def set_2_challenge_9():
    # given block, pad to 20-bytes
    block = b"YELLOW SUBMARINE"
    bytes_size = 20

    padded_block = pkcs7_pad(block, bytes_size)
    write_output("challenge_9_output.txt", padded_block)