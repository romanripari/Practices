'''
Código hecho por Roma
https://romanripari.ar
RomanRipari@gmail.com
En base a ejercicios del Curso de Python de la UNSAM.
'''

import random
import numpy as np

def nuevo_album(fig_en_el_album):
    return np.zeros(fig_en_el_album)

def esta_incompleto(A):
    return 0 in A

def nuevo_paquete(fig_en_el_album, fig_en_paquete):
    return random.choices(range(fig_en_el_album),k=fig_en_paquete)

def paquetes_necesarios(fig_en_el_album, fig_en_paquete, cambiazo):
    album = nuevo_album(fig_en_el_album)
    comprados = 0
    while esta_incompleto(album):
        comprados +=1
        paquete = nuevo_paquete(fig_en_el_album, fig_en_paquete)

        
        # Bloque Repetidas ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
        # En este bloque determinamos la lógica con la que se realizarían los intercambios.
        # En este caso, optamos por realizar un cambio por paquete, siempre que 
        # haya tocado al menos una repetida en el sobre.
        if cambiazo:
            repetidas = 0
            for p in paquete:
                if album[p - 1] == 1:
                    repetidas +=1
            #Si hay repetidas, se puede cambiar UNA por paquete
            if repetidas > 0:
                for i,a in enumerate(list(album)):
                    if a == 0:
                        paquete.append(i+1)
                        break
        # Bloque Repetidas ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑

        for p in paquete:
            album[p - 1] = 1
    return comprados

def test_paquetes(n, fig_en_el_album, fig_en_paquete, cambiafigu = False):
    Tests = [paquetes_necesarios(fig_en_el_album, fig_en_paquete, cambiafigu) for i in range(n)]
    return np.mean(Tests)

def run():
    #Datos Figuritas de Qatar (En septiembre de 2022)
    fig_en_el_album = 638
    fig_en_paquete = 5
    precio_paquete = 150
    precio_album = 650

    print("Si no se cambia ninguna figurita:")
    paquetes = int(test_paquetes(1000, fig_en_el_album, fig_en_paquete))
    print(f'Un álbum de {fig_en_el_album} figuritas se llena, en promedio,',
        f'comprando {paquetes:0.0f} paquetes.',
        f'Esto costaría ${(((paquetes) * precio_paquete) + precio_album):.2f}\n')
    
    print("Si se cambia una figurita cada vez que sale alguna repetida en el sobre:")
    paquetes = int(test_paquetes(1000, fig_en_el_album, fig_en_paquete, cambiafigu = True))
    print(f'Un álbum de {fig_en_el_album} figuritas se llena, en promedio,',
        f'comprando {paquetes:0.0f} paquetes.',
        f'Esto costaría ${(((paquetes) * precio_paquete) + precio_album):.2f}')
    
    #gráficos:
    # Se puede descomentar todo el siguiente bloque para ver en pantalla
    # un gráfico que muestra cómo se va llenando el álbum. 
    # Se nota una gran desaceleración al final.
'''
    import matplotlib.pyplot as plt
    
    plt.plot(calcular_historia_figus_pegadas(fig_en_el_album, precio_paquete))
    plt.xlabel("Cantidad de paquetes comprados.")
    plt.ylabel("Cantidad de figuritas pegadas.")
    plt.title("La curva de llenado se desacelera al final")
    plt.show()

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

def calcular_historia_figus_pegadas(fig_en_el_album, precio_paquete):
    album = nuevo_album(fig_en_el_album)
    historia_figus_pegadas = [0]
    while esta_incompleto(album):
        paquete = nuevo_paquete(fig_en_el_album, precio_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas
'''

if __name__ == "__main__":
    run()

