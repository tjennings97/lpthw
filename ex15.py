# import library
# sys is a package, argv is the feature in that package
from sys import argv

# set variables equal to command line arguments
script, filename = argv

# open the given file; returns a file object
txt = open(filename)

# use argv for filename
print(f"Here's your file {filename}")
print(txt.read())

# get filename from user
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

# close files, it's important to do so when done with them
txt.close()
txt_again.close()