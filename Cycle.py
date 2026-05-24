class Cycle:
    def __init__(self):
        self.elements:list[int] = []
    
    # Reorders this Cycle in-place to bring smallest element to front
    def reorder(self):
        while self.elements[0] != min(self.elements):
            self.shift_right()

    # Shifts all items in self.elements right by 1 index (wraps around)
    def shift_right(self):
        L = len(self.elements)
        tempElements = [0]*L

        for i in range(L):
            tempElements[(i+1) % L] = self.elements[i]

        self.elements = tempElements

    def __str__(self):
        self.reorder()
        return f'({" ".join(map(str, self.elements))})' 
    
    def __len__(self):
        return len(self.elements)
    
    def add(self, element:int):
        self.elements.append(element)