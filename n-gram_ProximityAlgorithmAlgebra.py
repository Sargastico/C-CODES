import math

fer = [[1,1,1,1,1,1,0,0,0,0,0,0,0]]

armando = [[0,0,0,0,1,1,1,1,1,0,0,0,0]]

dani = [[0,0,0,0,0,0,0,0,0,1,1,1,1]]

original = fer

def transposta(original):

    transposta = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]

    for i in range(len(original)):
        for j in range(len(original[0])):
            transposta[j][i] = original[i][j]

    return transposta


def produtoEscalar(original, transposta):

    resultado = 0

    for i in range(len(original)):
        for j in range(len(original[0])):
            resultado = resultado + (transposta[j][i] * fer[0][j])

    return resultado



transposta = transposta(original)

resultado = produtoEscalar(original, transposta)

moduloFer = 0
moduloOriginal = 0

for i in range(len(fer[0])):
    moduloFer = moduloFer + fer[0][i]**2

moduloFer = math.sqrt(moduloFer)

for j in range(len(original[0])):

    moduloOriginal = moduloOriginal + original[0][j]**2

moduloOriginal = math.sqrt(moduloOriginal)


diff = resultado/(moduloOriginal*moduloFer)
print(diff)
