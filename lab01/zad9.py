from itertools import groupby

napisy =  ["ala", "ma", "kota", "mikolaj", "prezenty"]
dict_of_len = {k: list(g) for k, g in groupby(sorted(napisy, key = len), len)}

print(dict_of_len)