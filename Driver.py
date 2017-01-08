import sys
import random
import os
import numpy as np
characters = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
              'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23,
              'Y': 24, 'Z': 25, 'a': 26, 'b': 27, 'c': 28, 'd': 29, 'e': 30, 'f': 31, 'g': 32, 'h': 33, 'i': 34,
              'j': 35, 'k': 36, 'l': 37, 'm': 38, 'n': 39, 'o': 40, 'p': 41, 'q': 42, 'r': 43, 's': 44, 't': 45,
              'u': 46, 'v': 47, 'w': 48, 'x': 49, 'y': 50, 'z': 51, ' ': 52}
reversedCharacters = characters.__class__(map(reversed, characters.items()))


# successful input: 2,3 3

# reads content from given file
def readFile(fileName):
    with open(fileName) as f:
        string = f.read()
    return string


# returns 1 if valid -1,-2,-3,-4,-5 if not(each error returns a different number)
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
    temp = plainText.replace('\n', '')
    if temp.isalpha() == 0:  # in case the message contains non alphabetic characters
        return -3
    if (len(temp) % (
                int(blockSize[0]) * int(blockSize[1]))) > 0:  # in case the message cannot be cut up into exact blocks
        return -4
    return 1


# turn characters matrix to numbers from character tables to encrypt(done)
def turnChar(matrix):
    converted = []
    matrix = np.array(matrix)
    for i in range(0, len(matrix)):
        converted.append(characters.__getitem__(matrix[i]))

    return converted


# turn numbers to Encrypted characters but returns it as an array
def getCypher(matrix):
    matrix = np.array(matrix)
    matrix = matrix.flatten()
    cypher = []
    for i in range(0, len(matrix)):
        cypher.append(reversedCharacters.__getitem__(matrix[i]))
    return cypher


# m = turnChar(np.array(["H","E","L","L","O"]))
# print m
# m=getCypher(m)
# print (m)

# to get encrypted array(done)
def Encrypt(message, key):
    key = np.mat(key)
    message = np.mat(message)
    key = key.astype(np.float)
    message = message.astype(np.float)
    cy = np.dot(key, message)
    cy %= 52
    return cy


# cc=Encrypt(A,np.mat("(1,44);(2,43)"))
# print cc
# function to reshape an array to n x m matrix
def getMatrix(matrix, N, M):
    matrix.reshape(N, M)
    return matrix


# return the overall encrypted text
# N & M are the key size
# M & B are the block size
# key is a string  and text is a string
def getEncryptedText(text, key, B, N, M):
    key = list(key)
    text = list(text)
    text = turnChar(text)
    key = turnChar(key)
    text = np.array(text)
    key = np.array(key)
    text = text.reshape(M, B)
    key = key.reshape(N, M)
    encryptedText = Encrypt(text, key)
    encryptedText = getCypher(encryptedText)
    return encryptedText


# text = "helloo"
# key =   "Hias"
# t=getEncryptedText(text,key,3,2,2)
# print t

def splitIntoBlocks(plainText, M, B):
    length = M * B
    index = 0
    blocks = []
    string = plainText.replace('\n', '')
    string += "$"
    while string[index] != "$":
        blocks.append(string[index:(index + length)])
        index += length
    return blocks


# plainText = "i love python\nyeah yo"
# MxB = ['2', '2']
# blocks = splitIntoBlocks(plainText, int(MxB[0]), int(MxB[1]))
# print(blocks)

while 1:  # key validity while loop
    # read content of (key.txt)
    key = readFile("key.txt")

    # Stage 1: Validate Key Size.
    # --get key size from user
    print("Please enter the key size.\n"
          "--Note: enter the coordinates in the format of 'N,M'\n"
          "--Note: both numbers must be greater or equal to 2\n"
          "Key size: ")
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
          "Block size: ")
    blockSize = sys.stdin.readline()
    blockSize = blockSize.rstrip('\n')
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

blocks = splitIntoBlocks(plainText, int(MxB[0]), int(MxB[1]))
originalText = plainText.split("\n")  # used later as a referance for where to add the new lines
