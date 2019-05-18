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
boyNames = process_textfile('boy_names.txt')
girlNames = process_textfile('girl_names.txt')

# Ranomize the list
finalBoyName = randomize_list(boyNames)
finalGirlName = randomize_list(girlNames)

# Print the final random names
print ("Selected Boy Name:",finalBoyName)
print ("Selected Girl Name:",finalGirlName)