# index 0 is a and 25 is z
ALPHABETS_MORSE_CODE = [
    ".-",
    "-...",
    "-.-.",
    "-..",
    ".",
    "..-.",
    "--.",
    "....",
    "..",
    ".---",
    "-.-",
    ".-..",
    "--",
    "-.",
    "---",
    ".--.",
    "--.-",
    ".-.",
    "...",
    "-",
    "..-",
    "...-",
    ".--",
    "-..-",
    "-.--",
    "--..",
]

# index 0 is 0 and 9 is 9
NUMBERS_MORSE_CODE = [
    "-----",
    ".----",
    "..---",
    "...--",
    "....-",
    ".....",
    "-....",
    "--...",
    "---..",
    "----.",
]


def main():
    alphabets_morse_code_dict = {
        chr(index + 97): code for index, code in enumerate(ALPHABETS_MORSE_CODE)
    }
    number_morse_code_dict = {
        str(index): code for index, code in enumerate(NUMBERS_MORSE_CODE)
    }
    str_to_converted = input("Enter string to convert to morse code:")
    str_to_converted = str_to_converted.lower()

    morse_str = ""

    for char in str_to_converted:
        if char in alphabets_morse_code_dict:
            converted_char = alphabets_morse_code_dict[char]
        elif char in number_morse_code_dict:
            converted_char = number_morse_code_dict[char]
        elif char == " ":
            converted_char = "/"
        else:
            converted_char = ""

        morse_str += converted_char
        if converted_char and not converted_char == "/":
            morse_str += "/"

    print("your morse code is: ")
    print(morse_str)


if __name__ == "__main__":
    main()
