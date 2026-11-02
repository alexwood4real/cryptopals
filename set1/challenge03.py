#######################################################################################################################
##### SET 1, CHALLENGE 3 ##############################################################################################
##### https://cryptopals.com/sets/1/challenges/3 ######################################################################

### Imports
from utils.encoding import decode_hex_string

# encoded hex string
ec_hex_string_s1c3 = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

def set_1_challenge_3():
    decode_hex_string(ec_hex_string_s1c3)