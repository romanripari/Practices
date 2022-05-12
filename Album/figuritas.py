import matplotlib.pyplot as plt
import random
import numpy as np

def nuevo_album(fig_en_el_album):
    return np.zeros(fig_en_el_album)

def esta_incompleto(A):
    return 0 in A

def nuevo_paquete(fig_en_el_album, fig_en_paquete):
    return random.choices(range(fig_en_el_album),k=fig_en_paquete)

def paquetes_necesarios(fig_en_el_album, fig_en_paquete):
    album = nuevo_album(fig_en_el_album)
    comprados = 0
    while esta_incompleto(album):
        comprados +=1
        paquete = nuevo_paquete(fig_en_el_album, fig_en_paquete)
        for p in paquete:
            album[p - 1] = 1
    return comprados
    
def test_paquetes(n, fig_en_el_album, fig_en_paquete):
    Tests = [paquetes_necesarios(fig_en_el_album, fig_en_paquete) for i in range(n)]
    return np.mean(Tests)

def grafico_llenado(fig_en_el_album, fig_en_paquete):
    album = nuevo_album(fig_en_el_album)
    historia_figus_pegadas = [0]
    while esta_incompleto(album):
        paquete = nuevo_paquete(fig_en_el_album, fig_en_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas

def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = nuevo_album(figus_total)
    historia_figus_pegadas = [0]
    while esta_incompleto(album):
        paquete = nuevo_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas

def run():
    #Datos Figuritas de Catar
    fig_en_el_album = 860
    fig_en_paquete = 5
    paquetes = test_paquetes(100, fig_en_el_album, fig_en_paquete)
    print(f'Un álbum de {fig_en_el_album} figuritas se llena, en promedio,',
        f'comprando {paquetes:0.0f} paquetes.',
        f'Esto costaría ${((paquetes) * 100 + 1746):.2f}')

    #gráficos:
    figus_total = 860
    figus_paquete = 5

    plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
    plt.xlabel("Cantidad de paquetes comprados.")
    plt.ylabel("Cantidad de figuritas pegadas.")
    plt.title("La curva de llenado se desacelera al final")
    plt.show()

if __name__ == "__main__":
    run()
