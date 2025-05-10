from datetime import datetime 
import benchmarking as bm
from metodos_ordenamiento import MetodosOrdenamiento
import matplotlib.pyplot as plt

if __name__ == "__main__":
    print("Funciona") 

    bench = bm.Benchmarking()
    metodos = MetodosOrdenamiento()
    
    tamanios = [5000, 10000, 30000, 50000, 100000]
    max_tamanio = 100000
    arreglo_completo = bench.build_arreglo(max_tamanio)
    resultados = []

    metodos_dic = {
        "Burbuja": metodos.sort_bubble,
        "Burbuja mejorado": metodos.sort_burbuja_mejorado_optimizado,
        "Seleccion": metodos.sort_seleccion,
        "Insercion": metodos.sort_insercion,
        "Shell": metodos.sort_Shell
    }

    for tam in tamanios:
        sub_arreglo = arreglo_completo[:tam]
        
        for nombre, fun_metodo in metodos_dic.items():
            tiempo_resultado = bench.medir_tiempo(fun_metodo, sub_arreglo.copy())
            print(f"Tamano: {tam}, Algoritmo: {nombre}, Tiempo: {tiempo_resultado:.3f} segundos") 
            resultados.append((tam, nombre, tiempo_resultado))

    # Procesamiento para gráfica
    tiempos_by_metodo = {
        "Burbuja": [],
        "Burbuja mejorado": [],      
        "Seleccion": [],
        "Insercion": [],
        "Shell": [],
    }

    for tam, nombre, tiempo in resultados: 
        tiempos_by_metodo[nombre].append(tiempo)

    plt.figure(figsize=(10,6))
    
    for nombre, tiempos in tiempos_by_metodo.items():
        plt.plot(tamanios, tiempos, label=nombre, marker="o")
    
    plt.title("Comparación de algoritmos de ordenamiento")
    plt.xlabel("Tamaño del arreglo")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()