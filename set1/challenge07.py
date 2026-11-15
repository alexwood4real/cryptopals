#######################################################################################################################
##### SET 1, CHALLENGE 7 ##############################################################################################
##### https://cryptopals.com/sets/1/challenges/7 ######################################################################

### Imports
import base64
from utils.blocks import decrypt_aes_128_ecb
from utils.file_io import read_input_raw, write_output

def set_1_challenge_7():
    # gather key and message as bytes
    key = b"YELLOW SUBMARINE"
    msg = base64.b64decode(read_input_raw("challenge_7.txt"))

    plaintext = decrypt_aes_128_ecb(key, msg)
    write_output("challenge_7_output.txt", plaintext.decode("utf-8"))