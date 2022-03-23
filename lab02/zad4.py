def replace(d, v, e):
    for key, value in d.items():
        if value == v:
            d[key] = e



d = {1:2, 3:4, 4:2}
replace(d,2,7)
print(d)