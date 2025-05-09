
class MetodosOrdenamiento:

    def sort_bubble(self , array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range (n):
            for j in range (0 , n-1-i):
               if arreglo [j] > arreglo [j+1]:
                   arreglo [j] , arreglo [j+1] = arreglo[j+1] , arreglo [j]
        return arreglo


    def sort_burbuja_mejorado_optimizado(self , array):  
        arreglo = array.copy()
        n = len(arreglo)
        for i in range (n):
           intercambiado = False
           for j in range (0, n-1-i):
               if arreglo [j] > arreglo [j+1]:       
                   arreglo [j] , arreglo [j+1] = arreglo[j+1] , arreglo [j] 
                   intercambiado = True
           if not intercambiado:
                break       
        return arreglo


    def sort_seleccion (self, array):
        arreglo = array.copy()
        n = len(arreglo)    
        for i in range (n):
            iM = i
            for j in range (i+1, n):
                if arreglo [iM] > arreglo [j]:
                    iM = j
            arreglo[i], arreglo[iM] = arreglo[iM], arreglo[i] 
        return arreglo
    

    def sort_Shell (self, array):
        arreglo = array.copy()
        n = len(arreglo)
        gap = n // 2 

        while gap > 0:
            for i in range(gap, n):
                temp = arreglo[i]
                j = i

               
                while j >= gap and arreglo[j - gap] > temp:
                    arreglo[j] = arreglo[j - gap]
                    j -= gap

                arreglo[j] = temp
            gap //= 2    
        
        return arreglo

    
    def sort_insercion(self, array):
        arreglo = array.copy()  
        n = len(arreglo)
    
        for i in range(1, n):  
            clave = arreglo[i]  
            j = i - 1           
               
            while j >= 0 and clave < arreglo[j]:
                arreglo[j + 1] = arreglo[j]
                j -= 1
        
            arreglo[j + 1] = clave  
    
        return arreglo


