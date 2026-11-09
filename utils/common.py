###################################
# Pure Common and Tool Operations #
###################################

### Imports 
from utils.xor import single_byte_xor
from utils.scoring import score_txt

### Functions

# performs XOR for every ascii key and return scores
def break_single_byte_xor(hex_str):
    cipher_bytes = bytes.fromhex(hex_str)

    candidates = []

    # iterate through all ascii codes
    for key in range(256):
        text = single_byte_xor(cipher_bytes, key)
        score = score_txt(text)

        candidates.append((score, key, text))

    candidates.sort(reverse=True)

    # return list of candidates is descending score order
    return candidates

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