#######################
# Pure XOR Operations #
#######################

### Constants

NEW_LINE = 10 

### Functions

# performs XOR on two fixed hexadecimal integers
def hex_xor(a, b):
    dec_a = int(a, 16)
    dec_b = int(b, 16)
    xor_val = dec_a ^ dec_b
    return hex(xor_val)

# performs XOR on a text with a definitive key
def repeating_key_byte_xor(msg, key):
    # set up the key info
    key_bytes = key.encode("utf-8")
    key_size = len(key)
    key_idx = 0

    # holds the encrypted message
    xor_msg = bytearray()

    # iterate through the message
    for byte in msg:
        # XOR the current byte with the current key byte and append
        msg_byte = byte ^ key_bytes[key_idx]

        # append the XORed byte to the encrypted message
        xor_msg.append(msg_byte)

        # iterate key
        key_idx += 1
        key_idx %= key_size

    # return encrypted msg as a hex string
    return xor_msg

# performs a XOR on every byte in a text with a single key
def single_byte_xor(cipher, key):
    return bytes( byte ^ key for byte in cipher)