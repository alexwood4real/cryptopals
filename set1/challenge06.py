#######################################################################################################################
##### SET 1, CHALLENGE 6 ##############################################################################################
##### https://cryptopals.com/sets/1/challenges/6 ######################################################################

### Imports
from utils.file_io import read_input_lines
from utils.xor import hamming_distance_xor

def set_1_challenge_6():
    # TODO: remove testing portion 
    text = read_input_lines("challenge_6_example.txt")

    # copy the two lines of text
    t1, t2 = text

    # turn the lines of text into bytes
    t1_bytes = t1.encode("utf-8")
    t2_bytes = t2.encode("utf-8")

    # print out the hamming-distance
    dist = hamming_distance_xor(t1_bytes, t2_bytes)
    print(dist)