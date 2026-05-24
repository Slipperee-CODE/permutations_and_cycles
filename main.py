from Permutation import Permutation

p1 = Permutation(0, 2, 1, 3, 4)

p2 = Permutation(1, 0, 2, 4, 3)

result = Permutation.compose(p1, p2)
# p2(0) -> 1 and p1(1) -> 2 so p1(p2(0)) -> 2 
# p2(1) -> 0 and p1(0) -> 0 so p1(p2(1)) -> 0 
# p2(2) -> 2 and p1(2) -> 1 so p1(p2(2)) -> 1 
# p2(3) -> 4 and p1(4) -> 4 so p1(p2(3)) -> 4 
# p2(4) -> 3 and p1(3) -> 3 so p1(p2(4)) -> 3 
# => result as a 1-line permutation is [2 0 1 4 3]

print(p1) # (1 2)

print(p2) # (0 1)(3 4)

print(result) # (0 1 2)(3 4)
