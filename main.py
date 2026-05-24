from Permutation import Permutation

p1 = Permutation(2, 1, 4, 3, 5)

p2 = Permutation(2, 4, 1, 5, 3)

result = Permutation.compose(p1, p2)
# p2(1) -> 2 and p1(2) -> 1 so p1(p2(1)) -> 1 
# p2(2) -> 4 and p1(4) -> 3 so p1(p2(2)) -> 3 
# p2(3) -> 1 and p1(1) -> 2 so p1(p2(3)) -> 2 
# p2(4) -> 5 and p1(5) -> 5 so p1(p2(4)) -> 5 
# p2(5) -> 3 and p1(3) -> 4 so p1(p2(5)) -> 4 
# => result as a 1-line permutation is [1 3 2 5 4]

print(p1) # (1 2)(3 4)

print(p2) # (1 2 4 5 3)

print(result) # (2 3)(4 5)
