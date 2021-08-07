# to run, enter 
#   python3 ex23.py utf-8 strict
#   python3 ex23.py utf-16 strict
import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)



def print_line (line, encoding, errors):
    # remove any leading and trailing spaces
    next_lang = line.strip()
    # decode bytes, encode strings
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


# opens a file, return the object
languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)