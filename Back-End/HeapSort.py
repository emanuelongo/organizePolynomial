import LinkedList

class Heap:
    def __init__(self, linkedList: LinkedList):
        return self.heapSort(linkedList) #PENSAR SI LLAMAR AL MÉTODO DÁNDOLE CADA LISTA POR SEPARADO
#PUEDE QUE NO NECESITE MOSTRAR DESDE ACÁ, MÁS FÁCIL MOSTRRA EL OBJETO EN LA VISTA
    def minHeap(self, list, lenght, i):
        
        largest = i 
        
        l = 2 * i + 1 
        
        r = 2 * i + 2  

        if l < lenght and list[l] > list[largest]:
            largest = l

        if r < lenght and list[r] > list[largest]:
            largest = r

        if largest != i:
            list[i], list[largest] = list[largest], list[i]

            self.minHeap(list, lenght, largest)

    def heapSort(self, list):
        
        lenght = len(list) 

        for i in range(lenght // 2 - 1, -1, -1):
            self.minHeap(list, lenght, i)

        for i in range(lenght - 1, 0, -1):
        
            list[0], list[i] = list[i], list[0] 

            self.minHeap(list, i, 0)
        
        return list