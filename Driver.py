import sys
import random
import os


# reads content from given file
def readFile(fileName):
    with open(fileName) as f:
        string = f.read()
    return string


# returns 1 if valid 0 isf not
def validateKeySize(keySize, key):
    if len(key) % 2 == 1:  # in case the key contains an odd number of characters
        return -1
    if key.isalpha() == 0:  # in case the key contains non alphabetic characters
        return -2
    if not (int(keySize[0]) * int(keySize[1]) == len(key)):  # in case the key contains non alphabetic characters
        return -3
    if (int(keySize[0]) < 2) or (int(keySize[1]) < 2):  # in case the key contains non alphabetic characters
        return -4
    return 1


while 1:  # key validity while loop
    # read content of files (key.txt) and (message.txt)
    key = readFile("key.txt")
    plainText = readFile("message.txt")

    # Stage 1: Validate Key size.
    # --get key size from user
    print("Please enter the key size.\n"
          "--Note: enter the coordinates in the format of 'N,M'\n"
          "--Note: both numbers must be greater or equal to 2\n"
          "Key size: ", end="")
    keySize = sys.stdin.readline()
    keySize = keySize.rstrip('\n')
    keySize = keySize.replace(' ', '')
    NxM = keySize.split(",")

    # --check if the key and the size given are valid
    validKey = validateKeySize(NxM, key)
    if (validKey == -1):
        print("\nThe given key in 'key.txt' file contains an odd number of characters, please update it and try again.")
        print("Do you want to try again?(y/n)")
        ans = sys.stdin.readline()
        ans = ans.rstrip('\n')
        ans = ans.replace(' ', '')
        if ans[0] == 'n':
            exit(0)
        else:
            continue
    elif (validKey == -2):
        print("\nThe given key in 'key.txt' file contains non-alphabetic characters, please update it and try again.")
        print("Do you want to try again?(y/n)")
        ans = sys.stdin.readline()
        ans = ans.rstrip('\n')
        ans = ans.replace(' ', '')
        if ans[0] == 'n':
            exit(0)
        else:
            continue
    elif (validKey == -3):
        print("\nThe given key size does not match up with the given key, please try again.")
        print("Do you want to try again?(y/n)")
        ans = sys.stdin.readline()
        ans = ans.rstrip('\n')
        ans = ans.replace(' ', '')
        if ans[0] == 'n':
            exit(0)
        else:
            continue
    elif (validKey == -4):
        print("\nThe given key size is too small, note that both numbers must be greater or equal to 2. "
              "Please try again.")
        print("Do you want to try again?(y/n)")
        ans = sys.stdin.readline()
        ans = ans.rstrip('\n')
        ans = ans.replace(' ', '')
        if ans[0] == 'n':
            exit(0)
        else:
            continue
    else:
        break
# end of key validity while loop

#hello zahra2