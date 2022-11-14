import argparse
from textwrap import wrap

def translate(raw_binary) -> int:
    """Translate a binary sequence
    to 8 bit ASCII chars."""
    binary = wrap(raw_binary, 8)
    translated = []
    for char in binary:
        an = list(char)
        a = 8
        num = 0
        for i in an:
            a -= 1
            num += (int(i)*(2**a))
        translated.append(chr(num))
    return translated
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Translate 8 bit binary sequence to its corresponding ASCII.")
    parser.add_argument("binary", type=str, nargs="+", help="Enter 8 bit binary sequence for translation.")
    # Example: python main.py 1011
    args = parser.parse_args()
    raw_binary = "".join(args.binary)
    if len(raw_binary)%8 == 0:
        print("".join(translate(raw_binary)))
    else:
        print("Each character must be 8 bits long.")
