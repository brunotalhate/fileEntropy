import math as mt
import sys


class dictionary(dict):
    def __init__(self):
        self = dict()

    def add(self, key):
        self[key] = 1

    def increment(self, key):
        self[key] += 1


bytesList = dictionary()
totalBytes = 0
entropy = 0

src = './files/file.txt'
if len(sys.argv) > 1:
    src = str(sys.argv[1])

print("File source:", src)

with open(src, "rb") as file:
    while True:
        charByte = ' '.join(format(x, 'b') for x in file.read(1))
        if charByte == '':
            break
        if charByte not in bytesList:
            bytesList.add(charByte)
        else:
            bytesList.increment(charByte)
        totalBytes += 1

print("Original file size:", totalBytes, "bytes")

for byte, qty in bytesList.items():
    prob = qty/totalBytes
    entropy -= prob * mt.log(prob, 2)

print("Entropy:", entropy, "bits per original byte")

minSize = mt.ceil(entropy * totalBytes)
minSizeBytes = minSize / 8
efficiency = (minSizeBytes / totalBytes) * 100

print("Minimum file size:", minSizeBytes, "bytes")
print("Efficiency of the original file:", efficiency, "%")
