#ZAD1
# grocery={}
# grocery={"mleko":1, "chleb":2}
# print(grocery)
# grocery["woda"]=5
# print(grocery)
# for val in grocery.values():
#     print(val)
# for key in grocery.keys():
#     print(key)

# cheer="Python rules!"
# print(cheer[0])
# print(cheer[7])
# print(cheer[-1])

# cheer="Python rules!"
# print(cheer[2:7:1])
# print(cheer[2:11:3])
# print(cheer[-2:-11:-3])

# lyrics ="happy birthday to you happy birthday to you happy birthday dear Happy birthday to you"
# counts={} #pusty sªownik
# words = lyrics.split(" ") #pobiera list¦ wszystkich sªów poprzez podzielenie ci¡gu w miejscach wyst¡pienia spacji
# for w in words:
#     w=w.lower() #zamienia na maªe litery
#     if w not in counts:
#         counts[w]=1
#     else:
#         counts[w]+=1
# print(counts)

# def powtórz(napis):
#     return napis+napis

# print(powtórz("Hello"))
#--------------------

#ZAD2
# def ispermutation(l1, l2):
#     if len(l1) != len(l2):
#         return False
#     else:
#         l1 = l1.sort()
#         l2 = l2.sort()

#         if l1 == l2:
#             return True

# l1 = [1,2,3,4]
# l2 = [4,3,2,1]

# print(ispermutation(l1, l2))
#--------------------

#ZAD3
# songs = {
#     "Hello": 1,
#     "Love": 5,
#     "Staying Alive": 6,
#     "Szampan": 3,
#     "Moglo byc nic": 5
# }

# titles = [k for k,v in songs.items() if v == 5]
# print(titles)
#--------------------

#ZAD4
# def replace(d, v, e):
#     for key, value in d.items():
#         if value == v:
#             d[key] = e



# d = {1:2, 3:4, 4:2}
# replace(d,2,7)
# print(d)
#--------------------


#ZAD5
# from collections import defaultdict
# def invert(d):
#     dinverted = defaultdict(list)
#     {dinverted[v].append(k) for k,v in d.items()}
#     dInv = dict(dinverted)
#     return dInv


# d1 = {1:2, 3:4, 5:6}
# d2 = {1:1, 3:1, 5:1}

# print(invert({1:2, 3:4, 5:6}))
# print(invert({1:1, 3:1, 5:1}))
#--------------------

#ZAD6
#--------------------


#ZAD7
#-------------------- https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/

#ZAD8
# https://www.geeksforgeeks.org/python-frequency-of-each-character-in-string/
text = "aplikacjebazodanowe"
result = {}
  
for char in text:
    result[char] = result.get(char, 0) + 1

print (f"Count of all characters in {text} is:\n {result}")


#ZAD9
# https://www.geeksforgeeks.org/python-maximum-frequency-character-in-string/#:~:text=We%20find%20maximum%20occurring%20character%20by%20using%20max()%20on%20values.&text=The%20most%20suggested%20method%20that,using%20max()%20on%20values.
# https://www.geeksforgeeks.org/c-program-find-second-frequent-character/
from collections import Counter
  
# initializing string 
text = "aplikacjebazodanowe"
result1 = Counter(text)
result = max(result1, key = result1.get)


# printing result 
print (f"The max1 and max2 of all characters in {text} is:\n max1: {result1}, max2: ...")