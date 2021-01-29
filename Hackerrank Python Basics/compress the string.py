
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
for k, g in groupby(input()):
    print("({}, {})".format(len(list(g)),k), end= " ")
