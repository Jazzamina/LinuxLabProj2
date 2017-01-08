import numpy as np

characters = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
              'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23,
              'Y': 24, 'Z': 25, 'a': 26, 'b': 27, 'c': 28, 'd': 29, 'e': 30, 'f': 31, 'g': 32, 'h': 33, 'i': 34,
              'j': 35, 'k': 36, 'l': 37, 'm': 38, 'n': 39, 'o': 40, 'p': 41, 'q': 42, 'r': 43, 's': 44, 't': 45,
              'u': 46, 'v': 47, 'w': 48, 'x': 49, 'y': 50, 'z': 51, ' ': 52}
# reverse Keys and values of dictionary
reversedCharacters = characters.__class__(map(reversed, characters.items()))

A = np.mat("(12,3);(13,4)")
B = np.mat("(43,53);(3,22)")


def generalizedEuclidianAlgorithm(a, b):
    if b > a:
        # print a, b
        return generalizedEuclidianAlgorithm(b, a);
    elif b == 0:
        return (1, 0);
    else:
        # print a,b
        (x, y) = generalizedEuclidianAlgorithm(b, a % b);
        return (y, x - (a / b) * y)


def inversemodp(a, p):
    a = a % p
    if (a == 0):
        print
        "a is 0 mod p"
        return 0
    (x, y) = generalizedEuclidianAlgorithm(p, a % p);
    return y % p


def identitymatrix(n):
    return [[int(x == y) for x in range(0, n)] for y in range(0, n)]


def inversematrix(matrix, q):
    n = len(matrix)
    A = np.matrix([[matrix[j, i] for i in range(0, n)] for j in range(0, n)], dtype=int)
    Ainv = np.matrix(identitymatrix(n), dtype=int)
    for i in range(0, n):
        factor = inversemodp(A[i, i], q)
        A[i] = A[i] * factor % q
        Ainv[i] = Ainv[i] * factor % q
        for j in range(0, n):
            if (i != j):
                factor = A[j, i]
                A[j] = (A[j] - factor * A[i]) % q
                Ainv[j] = (Ainv[j] - factor * Ainv[i]) % q
                # print A, Ainv
                # print i, j, factor
    return Ainv


def Encrypt(message, key):
    key = np.mat(key)
    message = np.mat(message)
    key = key.astype(np.float)
    message = message.astype(np.float)
    cy = np.dot(key, message)
    cy %= 53
    return cy


# turn numbers to Encrypted characters but returns it as an array
def getCypher(matrix):
    matrix = np.array(matrix)
    matrix = matrix.flatten()
    cypher = []
    for i in range(0, len(matrix)):
        cypher.append(reversedCharacters.__getitem__(int(matrix[i])))
    return cypher


# turn characters matrix to numbers from character tables to encrypt(done)
def turnChar(matrix):
    converted = []
    matrix = np.array(matrix)
    for i in range(0, len(matrix)):
        converted.append(characters.__getitem__(matrix[i]))

    return converted


# A = turnChar(A)
# B = turnChar(B)
# m=Encrypt(A,B)
# print m
# m=getCypher(m)
# print (m)


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

def Decrypt(message, key):
    key = np.mat(key)
    message = np.mat(message)
    key = key.astype(np.float)
    key = inversematrix(key, 53)
    print(key)
    message = message.astype(np.float)
    cy = np.dot(key, message)
    cy = cy.astype(np.int_)
    cy %= 53
    return cy


# return the overall decrypted text
# N & M are the key size
# M & B are the block size

# key is a string  and text is a string
def getDecryptedText(text, key, B, N, M):
    key = list(key)
    text = list(text)
    text = turnChar(text)
    key = turnChar(key)
    text = np.array(text)
    key = np.array(key)
    text = text.reshape(M, B)
    key = key.reshape(N, M)
    decryptedText = Decrypt(text, key)
    decryptedText = getCypher(decryptedText)
    return decryptedText


text = "SECU"
key = "RNDO"
t = getEncryptedText(text, key, 2, 2, 2)
print(t)
t = getDecryptedText(text, key, 2, 2, 2)
print(t)
