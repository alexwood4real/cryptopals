#######################################################################################################################
##### SET 1, CHALLENGE 4 ##############################################################################################
##### https://cryptopals.com/sets/1/challenges/4 ######################################################################

### Imports
from utils.xor import break_single_byte_xor
from utils.file_io import read_input_lines, write_output

def set_1_challenge_4():
    # hold the best score from each line
    best = []

    # iterate through the txt file
    lines = read_input_lines("challenge_4.txt")
    for line in lines:
        results = break_single_byte_xor(line)

        # record the highest score for this round
        best.append(results[0])

    best.sort(reverse=True)
    score, key, text = best[0]

    output = (
        f"Score: {score:.4f}\n"
        f"Key: {key} ({chr(key)})\n"
        f"Plaintext: {text.decode("ascii")}"
    )
    write_output("challenge_4_output.txt", output)
    