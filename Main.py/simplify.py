class simply:
    def __init__(self, list):
        self.list = list
        self.listValues = []
        self.simplifyList()

    def simplifyList(self):
        for i in range(len(self.list)):
            for j in range(self.list[i].length):
                vo = self.list[i].head
                self.listValues.append(vo.value)
                vo = vo.next
        
        return self.listValues