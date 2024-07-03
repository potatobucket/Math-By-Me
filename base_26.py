import re

base26 = {
    0 : "A",
    1 : "B",
    2 : "C",
    3 : "D",
    4 : "E",
    5 : "F",
    6 : "G",
    7 : "H",
    8 : "I",
    9 : "J",
    10 : "K",
    11 : "L",
    12 : "M",
    13 : "N",
    14 : "O",
    15 : "P",
    16 : "Q",
    17 : "R",
    18 : "S",
    19 : "T",
    20 : "U",
    21 : "V",
    22 : "W",
    23 : "X",
    24 : "Y",
    25 : "Z",
}
alphabet = {
    v : k for k, v in base26.items()
}
places = [
    1,
    26,
    676,
    17_576,
    456_976,
    11_881_376,
    308_915_776,
    8_031_810_176
]

testString = "aaaasome aaatimes aaaaabad aathings aahappen aaaaaand aaaaawho aaaaayou aaagonna aaaacall"

def convert_to_alphabase(number):
    """
Takes a decimal number and converts it to base-26 (a system where every digit is a letter A-Z of the standard Latin alphabet).
\nThe result will be a string eight digits long with leading As filling up space as needed. (ex. AAAAHOPE)
    """
    if number > 208_827_064_575:
        return "Error: number too big"
    else:
        place1 = int(number / places[0]) % 26
        place26 = int(number / places[1]) % 26
        place676 = int(number / places[2]) % 26
        place17_576 = int(number / places[3]) % 26
        place456_976 = int(number / places[4]) % 26
        place11_881_376 = int(number / places[5]) % 26
        place308_915_776 = int(number / places[6]) % 26
        place8_031_810_176 = int(number / places[7]) % 26
        return (
            f"{base26[place8_031_810_176]}{base26[place308_915_776]}{base26[place11_881_376]}{base26[place456_976]}{base26[place17_576]}{base26[place676]}{base26[place26]}{base26[place1]}"
            )

def convert_alpha_to_decimal(number):
    """
Returns a "number" of base-26 in its base-10 form.
\nThe number must be in the format of eight digits with leading As as needed (ex. AAAAHOPE)
    """
    if len(number) != 8:
        print("Error: alphabase string should be in the format AAAAAAAA (that's eight digits with leading As)")
    else:
        total = 0
        number = [letter for letter in number]
        for dIndex, digit in enumerate(number):
            total += alphabet[digit] * 26 ** ((dIndex - 7) * -1)
        return total

def encode(string, filename = "secret message.txt"):
    """
Encodes a string of base-26 "numbers" to their base-10 equivalents and saves them in a text file saved as filename.
\n(Default filename = "secret message.txt")
    """
    with open(filename, "w") as secret:
        splitString = string.split()
        convertedMessage = [convert_alpha_to_decimal(word) for word in splitString]
        for encode in convertedMessage:
            secret.write(f"{encode} ")

def decode(secret = "secret message.txt"):
    """Decodes a secret message (defaults to a text file named "secret message.txt") from base-10 to base-26."""
    with open(secret, "r") as decode:
        secretMessage = decode.read().split()
        decodedMessage = ""
        for code in range(len(secretMessage)):
            decodedMessage += re.sub(r"\bA{,7}", "", convert_to_alphabase(int(secretMessage[code]))) + " "
    return decodedMessage

# if __name__ == "__main__":
#     encode(testString.upper())
#     print(decode())
