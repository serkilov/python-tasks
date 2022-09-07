import string
import argparse


def caesar(text_string, step, alphabets):
    def shift(alphabet):
        return alphabet[step:] + alphabet[:step]

    shifted_alphabets = tuple(map(shift, alphabets))
    joined_aphabets = "".join(alphabets)
    joined_shifted_alphabets = "".join(shifted_alphabets)
    table = str.maketrans(joined_aphabets, joined_shifted_alphabets)
    return text_string.translate(table)


parser = argparse.ArgumentParser()
parser.add_argument("--text", type=str, required=True)
parser.add_argument("--key", type=int, required=True)
args = parser.parse_args()
text = args.text
key = args.key


alphabets_value = (string.ascii_lowercase, string.ascii_uppercase)

for char in text:
    if char not in "".join(alphabets_value):
        print(f"Incorrect symbol {char} detected")
        quit()

print(f"Input: {text}")
print(f"Key: {key}")
print(f"Result: {caesar(text, step=key, alphabets=alphabets_value)}")
