### Imports
import base64
from utils.xor import hex_xor

### Functions

# returns hex string to base64 string
def hex_to_64(num):
    raw_bytes = bytes.fromhex(num)
    encoded = base64.b64encode(raw_bytes)
    return encoded.decode("ascii")