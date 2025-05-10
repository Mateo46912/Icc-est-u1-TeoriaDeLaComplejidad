# Archivo principal main
from datetime import datetime 
import benchmarking as bm
from metodos_ordenamiento import MetodosOrdenamiento
import matplotlib.pyplot as plt
#import metodos_ordenamiento as ms
#from benchmarking import Benchmarking


if __name__ == "__main__":

    print ("Funciona") 

    bench = bm.Benchmarking()
    metodos = MetodosOrdenamiento()
    
    #tam = 1000
    #para practica crear solo un arreglo grande y ese dividirlo

    tamanios = [5000, 10000, 30000,50000,100000]
    resultados = []
    #max_tamanio = 100000

    for tam in tamanios:
        arreglo_base = bench.build_arreglo(tam)


        metodos_dic = {
        "Burbuja":metodos.sort_bubble,      
        "Burbuja mejorado" : metodos.sort_burbuja_mejorado_optimizado,      
        "Seleccion": metodos.sort_seleccion,
        "Shell": metodos.sort_Shell,
        "Insercion": metodos.sort_insercion
        }

    

        for nombre, fun_metodo in metodos_dic.items():                              
            tiempo_resultado = bench.medir_tiempo(fun_metodo, arreglo_base.copy())
            tupla_resultado = (tam, nombre, tiempo_resultado)
            resultados.append(tupla_resultado)

    for tam, nombre, tiempo_resultado in resultados:
        print(f"\n -TAMAÑO-: {tam} , --NOMBRE METODO--: {nombre}, -TIEMPO-: {tiempo_resultado: .6f} segundos") 

    tiempos_by_metodo = {
        "Burbuja":[],
        "Burbuja mejorado" : [],      
        "Seleccion": [],
        "Shell": [],
        "Insercion": [],

    }


    for tam,nombre,tiempo in resultados: 
        tiempos_by_metodo[nombre].append(tiempo)

    plt.figure(figsize = (10,6))


    for nombre, tiempos in tiempos_by_metodo.items():
        plt.plot(tamanios, tiempos, label= nombre , marker ="o")



    
    plt.title("Comparación de algoritmos de ordenamiento")
    plt.xlabel ("Tamaño del arreglo")
    plt.ylabel("Tiempo de ejecución (s)")

 
    plt.legend()
    plt.grid(True)
    plt.tight_layout
    
    plt.show()
    







