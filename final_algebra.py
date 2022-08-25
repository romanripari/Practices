import matplotlib.pyplot as plt
import random
import numpy as np

def experimento(n, respondo):
    c = [1,2,3,4]
    notas = []
    for i in range(n):
        correctas = []
        for j in range(respondo):
            respuesta = random.choice(c)
            if respuesta == 1:
                correctas.append(True)
            else:
                correctas.append(False)
        notas.append(correctas)
    return notas

def run(tam):
    resultado = experimento(10000, tam)
    apruebo = 0
    desapruebo = 0
    for r in resultado:
        correctas = sum(r)
        incorrectas = len(r)-sum(r)
        if correctas >= 8 and correctas >= incorrectas:
            apruebo +=1
        else:
            desapruebo +=1
    return apruebo/desapruebo

if __name__ == "__main__":
    exper = []
    for t in range(20):
        exper.append(run(t))
    plt.plot(exper)
    plt.show()
