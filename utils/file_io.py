############################
# Pure File I/O Operations #
############################

### Imports
from pathlib import Path

### Constants 

# Root directory
ROOT_DIR = Path(__file__).resolve().parent.parent

# Input and Output directories
INPUT_DIR = ROOT_DIR / "inputs"
OUTPUT_DIR = ROOT_DIR / "outputs"

### Functions

# read inputs from file
def read_input(filename):
    file_path = INPUT_DIR / filename
    return file_path.read_text(encoding="utf-8").strip()

# reads multiple lines from file and returns as a list
def read_input_lines(filename):
    file_path = INPUT_DIR / filename
    return file_path.read_text(encoding="utf-8").splitlines()

# read multiple lines from a file and returns as one long string
def read_input_raw(filename):
    file_path = INPUT_DIR / filename
    return file_path.read_text(encoding="utf-8")

# write output to file
def write_output(filename, data):
    file_path = OUTPUT_DIR / filename
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(str(data), encoding="utf-8")