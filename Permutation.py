from Cycle import Cycle

class Permutation:
    # Takes a permutation in 1-line notation as "elements"
    def __init__(self, *elements):
        self.elements:list[int] = list(elements)

    # Finds the permutation resulting from composing p1 and p2
    # Uses right to left composition
    @staticmethod
    def compose(p1:"Permutation", p2:"Permutation") -> "Permutation":
        resultingPermutation = []
        for i in range(len(p1)):
            resultingPermutation.append(p1[p2[i]])

        return Permutation(*resultingPermutation)
    
    # Gets all cycles formed by this permutation
    def getAllCycles(self) -> list[Cycle]:
        allCycles = []
        unused = self.elements[:]
        while unused:
            curr = unused[0]
            currCycle = Cycle()
            while curr in unused:
                currCycle.add(curr)
                unused.remove(curr)
                curr = self.elements[curr]
            allCycles.append(currCycle)
        return allCycles
    
        # Returns this Permutation in cycle notation
    
    def __str__(self):
        allCycles = map(str,
            filter(lambda c: len(c) > 1,
                sorted(self.getAllCycles(), 
                    key=len, reverse=True
                )
            )
        )
        return "".join(allCycles)
    
    def __len__(self):
        return len(self.elements)

    def __getitem__(self, key):
        return self.elements[key]
    