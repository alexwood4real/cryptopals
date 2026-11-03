#######################################################################################################################
##### SET 1, CHALLENGE 1 ##############################################################################################
##### https://cryptopals.com/sets/1/challenges/1 ######################################################################

### Imports
from utils.encoding import hex_to_64
from utils.file_io import read_input, write_output

def set_1_challenge_1():
    hex_str = read_input("challenge_1.txt")
    write_output("challenge_1_output.txt", str(hex_to_64(hex_str)))