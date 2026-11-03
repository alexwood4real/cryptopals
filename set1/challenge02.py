#######################################################################################################################
##### SET 1, CHALLENGE 2 ##############################################################################################
##### https://cryptopals.com/sets/1/challenges/2 ######################################################################

### Imports
from utils.xor import hex_xor
from utils.file_io import read_input_lines, write_output

def set_1_challenge_2():
    hex_str_1, hex_str_2 = read_input_lines("challenge_2.txt")
    write_output("challenge_2_output.txt", str(hex_xor(hex_str_1, hex_str_2)))