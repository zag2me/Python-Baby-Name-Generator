# Import any modules we need
import random

# A function to read a text file of baby names
def process_textfile(textfile):
    f = open(textfile, 'r')
    names = f.read().splitlines()
    f.close()
    return names

def randomize_list(myList):
    random.shuffle(myList)    
    finalName = myList[0]
    return finalName

################
# Main program #
################

# Read the text file
x = process_textfile('baby_names.txt')
# Ranomize the list
finalName = randomize_list(x)
# Print the final random name
print (finalName)