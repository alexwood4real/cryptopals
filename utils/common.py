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
    return candidates

def calc_key_len(msg):
    # try keysize lengths from 2-40
    candidates = []
    for keysize_it in range(1, 41):
        # take the first four KEYSIZE worth of bytes
        blocks = [
            msg[i * keysize_it:(i + 1) * keysize_it]
            for i in range(4)
        ]

        # find the hamming distance between the two blocks and normalize
        ham = 0
        for i in range(len(blocks) - 1):
            ham += hamming_distance(blocks[i], blocks[i + 1])
        norm = ham / (3 * keysize_it)
        candidates.append((norm, keysize_it))

    # 3. return the 5 key size with the smallest hamming distance
    candidates.sort()
    result = [key_data[1] for key_data in candidates[:5]]
    return result

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

# transpose the msg into blocks for the respective keysize
# block_idx : (msg[block_idx + n*key_size]), while (block_idx + n*keysize) < len(msg)
# block_list = [
# 0   : (msg[0 + 0*key_size], msg[0 + 1*key_size], msg[0 + 2*keysize], ...)
# 1   : (msg[1 + 0*key_size], msg[1 + 1*key_size], msg[1 + 2*keysize], ...)
# ...
# n-1 : (msg[(n-1) + 0*key_size], msg[(n-1) + 1*key_size], msg[(n-1) + 2*key_size], ...)
# ]
def transpose_msg(msg, key_sizes):
    block_list = []
    for key_size in key_sizes:
        candidate_blocks = []
        for block_idx in range(key_size):
            block = []
            it = 0
            while (block_idx + (it * key_size)) < len(msg):
                block.append(msg[(block_idx + (it * key_size))])
                it += 1
            candidate_blocks.append(bytes(block))
        block_list.append(candidate_blocks)
    return block_list