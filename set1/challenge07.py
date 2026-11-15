#######################################################################################################################
##### SET 1, CHALLENGE 7 ##############################################################################################
##### https://cryptopals.com/sets/1/challenges/7 ######################################################################

### Imports
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from utils.file_io import read_input_raw, write_output

def set_1_challenge_7():
    # gather key and message as bytes
    key = b"YELLOW SUBMARINE"
    msg = base64.b64decode(read_input_raw("challenge_7.txt"))

    # create the AES-128 in ECB mode descryptor with the key
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    decryptor = cipher.decryptor()

    # decrypt message and return as string
    plaintext = decryptor.update(msg) + decryptor.finalize()
    write_output("challenge_7_output.txt", plaintext.decode("utf-8"))