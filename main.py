import argparse
from textwrap import wrap

def translate(raw_binary) -> List:
    """Translate a binary sequence
    to 8 bit ASCII chars."""
    binary = wrap(raw_binary, 8) # Returns binary to a split list of 8 bits per entry.
    translated = [] 

    for char in binary:
        byte = list(char)
        a = 8
        num = 0
        for bit in byte:
            a -= 1
            num += (int(bit)*(2**a))

        translated.append(chr(num)) # Chr get unicode string from integer we derived from binary.

    return translated
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Translate 8 bit binary sequence to its corresponding ASCII.")
    parser.add_argument("binary", type=str, nargs="+", help="Enter 8 bit binary sequence for translation.")
    # Example: python main.py 1011
    args = parser.parse_args()
    raw_binary = "".join(args.binary) # Argparser sees every space between chars as another arg. This line allows us to join every byte if there is more than one.
    if len(raw_binary) % 8 == 0: # Checks if the bytes given combined are divisible by 8 (number of bits per byte).
        print("".join(translate(raw_binary)))
    else:
        print("Each character must be 8 bits long.")
