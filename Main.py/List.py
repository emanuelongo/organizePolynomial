class main:
  def __init__(self, polynomial: str):
    self.polynomial = polynomial
    self.exponentsList = []
    self.objectsLinkedList = []
    self.separatePolynomial()
    self.connectLists()
    self.printPolynomial()

  def separatePolynomial(self):
    for i in range(len(self.polynomial)):
      if self.polynomial[i] == "x" and self.polynomial[i + 1] == "*" and (self.polynomial[i + 2] not in self.exponentsList): #NO ESTÁ EL EXPONENTE REGISTRADO Y MAYOR QUE 1
        self.exponentsList.append(self.polynomial[i + 2])
        objectList = LinkedList()
        objectList.append(self.polynomial[i - 2] + self.polynomial[i - 1])
        self.objectsLinkedList.append(objectList)
      elif self.polynomial[i] == "x" and self.polynomial[i + 1] == "*" and (self.polynomial[i + 2] in self.exponentsList): #EL EXPONENTE ESTÁ REGISTRADO Y MAYOR QUE 1
        for j in range(len(self.exponentsList)):
          if self.exponentsList[j] == self.polynomial[i + 2]:
            self.objectsLinkedList[j].append( self.polynomial[i - 2] + self.polynomial[i - 1])
      
  def connectLists(self):
    n = len(self.exponentsList)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if self.exponentsList[j] > self.exponentsList[j + 1]:
                self.exponentsList[j], self.exponentsList[j + 1] = self.exponentsList[j + 1], self.exponentsList[j]
                self.objectsLinkedList[j], self.objectsLinkedList[j + 1] = self.objectsLinkedList[j + 1], self.objectsLinkedList[j]
                swapped = True
        if (swapped == False):
            break
  
  def printPolynomial(self):
    listReceptor = ""
    for n in range(len(self.objectsLinkedList)):
      listReceptor += f"{self.objectsLinkedList[n]}x*{self.exponentsList[n]}"
    
    return listReceptor

class Node:
  __slots__ = 'value', 'next'

  def __init__(self, value):
    self.value = value
    self.next = None

  def __str__(self):
    return str(self.value)
  
class LinkedList:

  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def __iter__(self):
    curr_node = self.head
    while curr_node is not None:
      yield curr_node
      curr_node = curr_node.next

  def __str__(self):
    result = [str(x.value) for x in self]
    return ' '.join(result)

  def append(self, value):
    new_node = Node(value)
    if self.head == None:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = None
      self.tail.next = new_node
      self.tail = new_node
    self.length += 1