
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
s, k  = input().upper().split()
comb = combinations_with_replacement(sorted(s), int(k))
for i in comb:
    print("".join(i))
