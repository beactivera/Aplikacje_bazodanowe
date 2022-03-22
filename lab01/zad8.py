test_list = [1, 6, 7, 9, 9, 2, 4, 5]

print("Oryginalna lista: " + str(test_list))

even_i = []
for i in range(0, len(test_list)):
    if i % 2 == 0:
        even_i.append(test_list[i])
 
print("Elementy z listy na parzystych miejscach: " + str(even_i))