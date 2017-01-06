import sys
import random
import os

# successful input: 2,3 3

# reads content from given file
def readFile(fileName):
    with open(fileName) as f:
        string = f.read()
    return string


# returns 1 if valid -1,-2,-3,-4 if not(each error returns a different number)
def validateKeySize(keySize, key):
    if (keySize[0].isdigit() == 0) or (
        keySize[1].isdigit() == 0):  # in case the key size contains non numeric characters
        return -5
    if len(key) % 2 == 1:  # in case the key contains an odd number of characters
        return -1
    if key.isalpha() == 0:  # in case the key contains non alphabetic characters
        return -2
    if not (int(keySize[0]) * int(keySize[1]) == len(
            key)):  # in case the desired key size does not match up with the key in length
        return -3
    if (int(keySize[0]) < 2) or (int(keySize[1]) < 2):  # in case the key rows or columns are less than 2
        return -4
    return 1


# returns 1 if valid -1,-2,-3,-4 if not(each error returns a different number)
def validateBlockSize(blockSize, plainText):
    if blockSize[1].isdigit() == 0:  # in case the block size contains non numeric characters
        return -2
    if int(blockSize[1]) < 2:  # in case the key rows or columns are less than 2
        return -1
    temp = plainText.replace(' ', '')
    temp = temp.replace('\n', '')
    if temp.isalpha() == 0:  # in case the message contains non alphabetic characters
        return -3
    if (len(temp) % (int(blockSize[0]) * int(blockSize[1]))) > 0:  # in case the message cannot be cut up into exact blocks
        return -4
    return 1


while 1:  # key validity while loop
    # read content of (key.txt)
    key = readFile("key.txt")

    # Stage 1: Validate Key Size.
    # --get key size from user
    print("Please enter the key size.\n"
          "--Note: enter the coordinates in the format of 'N,M'\n"
          "Key size: ", end="")
    keySize = sys.stdin.readline()
    keySize = keySize.rstrip('\n')
    keySize = keySize.replace(' ', '')
    NxM = keySize.split(",")
    # --check if the key and the size given are valid
    validKey = validateKeySize(NxM, key)
    if validKey == -1:
        print("\nThe given key in 'key.txt' file contains an odd number of characters, "
              "please make the necessary changes and try again.")
        print("Do you want to try again?(y/n)")
        ans = sys.stdin.readline()
        ans = ans.rstrip('\n')
        ans = ans.replace(' ', '')
        if ans[0] == 'n':
            exit(0)
        else:
            continue
    elif validKey == -2:
        print("\nThe given key in 'key.txt' file contains non-alphabetic characters, "
              "please make the necessary changes and try again.")
        print("Do you want to try again?(y/n)")
        ans = sys.stdin.readline()
        ans = ans.rstrip('\n')
        ans = ans.replace(' ', '')
        if ans[0] == 'n':
            exit(0)
        else:
            continue
    elif validKey == -3:
        print("\nThe given key size does not match up with the given key, please try again.")
        print("Do you want to try again?(y/n)")
        ans = sys.stdin.readline()
        ans = ans.rstrip('\n')
        ans = ans.replace(' ', '')
        if ans[0] == 'n':
            exit(0)
        else:
            continue
    elif validKey == -4:
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
    elif validKey == -5:
        print("\nThe given key size contains non-numeric characters, please try again.")
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

while 1:  # block validity while loop
    # Read content of (message.txt)
    plainText = readFile("message.txt")

    # Stage 2: Enter Block Size.
    # --get block size from user
    print("Please enter the desired number of columns in the blocks.\n"
          "--Note: the number of rows will be taken from the key"
          "(the number of columns of the key must equal the number of rows in the block.)\n"
          "Block size: ", end="")
    blockSize = sys.stdin.readline()
    blockSize = blockSize.rstrip('\n')
    blockSize = blockSize.replace(' ', '')
    MxB = [NxM[1], blockSize]
    # --check if the desired block size is valid
    validBlock = validateBlockSize(MxB, plainText)
    if validBlock == -1:
        print("\nThe given block size is too small, note that the number must be greater or equal to 2. "
              "Please try again.")
        print("Do you want to try again?(y/n)")
        ans = sys.stdin.readline()
        ans = ans.rstrip('\n')
        ans = ans.replace(' ', '')
        if ans[0] == 'n':
            exit(0)
        else:
            continue
    elif validBlock == -2:
        print("\nThe given block size contains non-numeric characters, please try again.")
        print("Do you want to try again?(y/n)")
        ans = sys.stdin.readline()
        ans = ans.rstrip('\n')
        ans = ans.replace(' ', '')
        if ans[0] == 'n':
            exit(0)
        else:
            continue
    elif validBlock == -3:
        print("\nThe given message in 'message.txt' file contains non-alphabetic characters, "
              "please make the necessary changes and try again.")
        print("Do you want to try again?(y/n)")
        ans = sys.stdin.readline()
        ans = ans.rstrip('\n')
        ans = ans.replace(' ', '')
        if ans[0] == 'n':
            exit(0)
        else:
            continue
    elif validBlock == -4:
        print("\nThe message cannot be cut up in exact blocks of the size you asked for. "
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
# end of block validity while loop
