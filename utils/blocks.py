###############################
# Pure ECB Related Operations #
###############################

### Imports
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

# decrypt message with key from AES-128 in CBC mode
def decrypt_aes_128_cbc(key, msg, iv):
    # create the AES-128 in ECB mode descryptor with the key
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()

    # decrypt message and return as string
    plaintext = decryptor.update(msg) + decryptor.finalize()
    return plaintext

# decrypt message with key from AES-128 in ECB mode
def decrypt_aes_128_ecb(key, msg):
    # create the AES-128 in ECB mode descryptor with the key
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    decryptor = cipher.decryptor()

    # decrypt message and return as string
    plaintext = decryptor.update(msg) + decryptor.finalize()
    return plaintext

# encrypt message with key from AES-128 in CBC mode
def encrypt_aes_128_cbc(key, msg, iv):
    # create the AES-128 in ECB mode descryptor with the key
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    enncryptor = cipher.encryptor()

    # decrypt message and return as string
    plaintext = enncryptor.update(msg) + enncryptor.finalize()
    return plaintext

# encrypt message with key from AES-128 in ECB mode
def encrypt_aes_128_ecb(key, msg):
    # create the AES-128 in ECB mode descryptor with the key
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    encryptor = cipher.encryptor()

    # decrypt message and return as string
    plaintext = encryptor.update(msg) + encryptor.finalize()
    return plaintext

# determine if given message was encoded with ECB mode
def is_aes_ecb(msg_bytes):
    # split each line into 16 blocks
    blocks = [
        msg_bytes[i:i + 16]
        for i in range(0, len(msg_bytes), 16)
    ]

    # if any duplicate blocks exist, that line is ecrypted in ECB mode
    if len(blocks) != len(set(blocks)):
        return True
    else:
        return False

# pad block using PKCS#7 size pad_bytes
def pkcs7_pad(block, pad_bytes):
    # determine number of bits to pad to 
    pad_bits = pad_bytes * 8

    # pad the block to the given number of bytes and return
    padder = padding.PKCS7(pad_bits).padder()
    padded_data = padder.update(block) + padder.finalize()
    return padded_data