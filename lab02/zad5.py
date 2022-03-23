from collections import defaultdict
def invert(d):
    dinverted = defaultdict(list)
    {dinverted[v].append(k) for k,v in d.items()}
    dInv = dict(dinverted)
    return dInv


d1 = {1:2, 3:4, 5:6}
d2 = {1:1, 3:1, 5:1}

print(invert({1:2, 3:4, 5:6}))
print(invert({1:1, 3:1, 5:1}))