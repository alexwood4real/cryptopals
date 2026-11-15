#######################################################################################################################
##### SET 1, CHALLENGE 6 ##############################################################################################
##### https://cryptopals.com/sets/1/challenges/6 ######################################################################

### Imports
import base64
from utils.file_io import read_input_raw
from utils.common import break_single_byte_xor, calc_key_len, hamming_distance, transpose_msg

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
    msg = base64.b64decode(read_input_raw("challenge_6.txt"))

    # 1. try keysize lengths from 2-40
    candidates = []
    for keysize_it in range(2, 41):
        # 2. Take the first and second KEYSIZE worth of bytes
        block_1 = msg[:keysize_it]
        block_2 = msg[keysize_it: 2 * keysize_it]

        # find the hamming distance between the two blocks and normalize
        ham = hamming_distance(block_1, block_2)
        norm = ham / keysize_it
        print(f"norm: {norm}\n size: {keysize_it}\n\n")
        candidates.append((norm, keysize_it))

    # 3. select the key size with the smallest hamming distance
    candidates.sort()
    key_size = candidates[0][1]
    # TODO: when done, replace top portion with single command
    # key_size = calc_key_len(msg)

    # 4. transpose the blocks for the respective keysize
    # block_idx : (msg[block_idx + n*key_size]), while (block_idx + n*keysize) < len(msg)
    # block_list = [
    # 0 : (msg[0 + 0*key_size], msg[0 + 1*key_size], msg[0 + 2*keysize], ...)
    # 1 : (msg[1 + 0*key_size], msg[1 + 1*key_size], msg[1 + 2*keysize], ...)
    # ...
    # key_size - 1 : (msg[(key_size - 1) + 0*key_size], msg[(key_size - 1) + 1*key_size], ...)
    # ]
    block_list = []
    for block_idx in range(key_size):
        block = []
        it = 0
        while (block_idx + (it * key_size)) < len(msg):
            block.append(msg[(block_idx + (it * key_size))])
            it += 1
        block_list.append(block)
    # TODO: when done, replace top portion with single command
    # block_list = transpose_msg(msg, key_size)

    # 5. perform break_single_byte_xor on each block idx to solve for that key
    key = ""
    for l_it in range(key_size):
        l_list = bytes(block_list[l_it])
        l = break_single_byte_xor(l_list)
        key += chr(l[0][1])
    print(key)
