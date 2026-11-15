###################################
# Pure Common and Tool Operations #
###################################

### Imports 
from utils.xor import single_byte_xor
from utils.scoring import score_txt

### Functions

# performs XOR for every ascii key and return scores
def break_single_byte_xor(cipher_bytes):
    candidates = []

    # iterate through all ascii codes
    for key in range(256):
        text = single_byte_xor(cipher_bytes, key)
        score = score_txt(text)

        candidates.append((score, key, text))

    candidates.sort(reverse=True)

    # return list of candidates is descending score order
    # TODO: when done, just return the top one not the list
    return candidates

def calc_key_len(msg):
    candidates = []
    for keysize_it in range(2, 41):
        # take the first and second KEYSIZE worth of bytes
        block_1 = msg[:keysize_it]
        block_2 = msg[keysize_it: 2 * keysize_it]

        # find the hamming distance between the two blocks and normalize
        ham = hamming_distance(block_1, block_2)
        norm = ham / keysize_it
        candidates.append((norm, keysize_it))

    # return the key size with the smallest hamming distance
    candidates.sort()
    return candidates[0][1]

# performs XOR on numbers to find differing bits
def hamming_distance(bytes_1, bytes_2):
    # lengths must be the same
    if len(bytes_1) != len(bytes_2):
        raise ValueError("Length of strings not equal")

    # iterate through both strings performing xor on each char individually
    bytes_length = len(bytes_1)
    bit_cnt = 0
    for idx in range(bytes_length):
        # count the number of differing bits per XORed char
        xor_bits = bytes_1[idx] ^ bytes_2[idx]
        bit_cnt += xor_bits.bit_count()

    return bit_cnt

def is_readable(data, threshold=0.90):
    readable = sum(
        byte in (9, 10, 13) or 32 <= byte <= 126
        for byte in data
    )

    return readable / len(data) >= threshold

# transpose the msg into blocks for the respective keysize
# block_idx : (msg[block_idx + n*key_size]), while (block_idx + n*keysize) < len(msg)
# block_list = [
# 0   : (msg[0 + 0*key_size], msg[0 + 1*key_size], msg[0 + 2*keysize], ...)
# 1   : (msg[1 + 0*key_size], msg[1 + 1*key_size], msg[1 + 2*keysize], ...)
# ...
# n-1 : (msg[(n-1) + 0*key_size], msg[(n-1) + 1*key_size], msg[(n-1) + 2*key_size], ...)
# ]
def transpose_msg(msg, n):
    block_list = []
    for block_idx in range(n):
        block = []
        it = 0
        while (block_idx + (it * n)) < len(msg):
            block.append(msg[(block_idx + (it * n))])
            it += 1
        block_list.append(block)
    return block_list