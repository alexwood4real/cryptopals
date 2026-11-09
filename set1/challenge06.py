#######################################################################################################################
##### SET 1, CHALLENGE 6 ##############################################################################################
##### https://cryptopals.com/sets/1/challenges/6 ######################################################################

### Imports
from utils.file_io import read_input_lines
from utils.common import hamming_distance

### Steps to take 
## 1. Let KEYSIZE be the guessed length of the key; trying values 2-40
## 2. For each KEYSIZE take the first KEYSIZE worth of bytes and the second KEYSIZE worth of bytes,
#     find the hamming-distance between them, and divide the result by KEYSIZE to normalize.
#     The KEYSIZE with the smallest normalized edit distance is probably the key
## 3. Break the text into blocks of KEYSIZE lengths
## 4. Transpose blocks:
#     make a block that is the first byte of every block,
#     and a block that is the second byte of every block...
## 5. Solve each block as if it was a single byte XOR with single_byte_xor
## 6. For each block, the sinlge-byte XOR key that produces the best looking histogram is the 
#     repeating XOR key byte for that block
## 7. Put them together, and that is the key. Can then decrypt with repeating_key_byte_xor


def set_1_challenge_6():
    msg = read_input_lines("challenge_6.txt")

    # 1. try keysize lengths from 2-40
    for keysize_it in range(2, 41):
        pass