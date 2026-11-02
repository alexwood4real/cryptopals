# performs XOR on two fixed buffers of equal length
def hex_xor(a, b):
    dec_a = int(a, 16)
    dec_b = int(b, 16)
    xor_val = dec_a ^ dec_b
    return str(hex(xor_val))