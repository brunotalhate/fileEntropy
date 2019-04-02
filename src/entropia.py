import math as mt
import sys


class dictionary(dict):
    def __init__(self):
        self = dict()

    def adiciona(self, key):
        self[key] = 1

    def incrementa(self, key):
        self[key] += 1


bytesList = dictionary()
quantidadeTotalBytes = 0
entropia = 0

arquivo = './files/file.txt'
if len(sys.argv) > 1:
    arquivo = str(sys.argv[1])

print("Analisando o arquivo em:", arquivo)

with open(arquivo, "rb") as file:
    while True:
        charByte = ' '.join(format(x, 'b') for x in file.read(1))
        if charByte == '':
            break
        if charByte not in bytesList:
            bytesList.adiciona(charByte)
        else:
            bytesList.incrementa(charByte)
        quantidadeTotalBytes += 1

print("Tamanho original do arquivo:", quantidadeTotalBytes, "bytes")

for binario, nRepeticoes in bytesList.items():
    prob = nRepeticoes/quantidadeTotalBytes
    entropia -= prob * mt.log(prob, 2)

print("Entropia:", entropia, "bits por símbolo")

tamanhoMinimo = mt.ceil(entropia * quantidadeTotalBytes)
minimoEmBytes = tamanhoMinimo / 8
eficiencia = (minimoEmBytes / quantidadeTotalBytes) * 100

print("Tamanho mínimo do arquivo:", minimoEmBytes, "bytes")
print("Eficiência do arquivo original:", eficiencia, "%")
