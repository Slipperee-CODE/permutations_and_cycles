class Cycle:
    def __init__(self):
        self.elements:list[int] = []
    
    def __str__(self):
        return f'({" ".join(map(str, sorted(self.elements)))})' 
    
    def __len__(self):
        return len(self.elements)
    
    def add(self, element:int):
        self.elements.append(element)