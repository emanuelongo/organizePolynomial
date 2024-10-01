class Heap:
    def __init__(self, linkedList):
        self.heapSort(linkedList) #PENSAR SI LLAMAR AL MÉTODO DÁNDOLE CADA LISTA POR SEPARADO

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
        
        lenght = list.lenght() 

        for i in range(lenght // 2 - 1, -1, -1):
            self.minHeap(list, lenght, i)

        for i in range(lenght - 1, 0, -1):
        
            list.head, list[i] = list[i], list.head 

            self.minHeap(list, i, 0)
        
        return list