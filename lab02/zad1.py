grocery={}
grocery={"mleko":1, "chleb":2}
print(grocery)
grocery["woda"]=5
print(grocery)
for val in grocery.values():
    print(val)
for key in grocery.keys():
    print(key)

cheer="Python rules!"
print(cheer[0])
print(cheer[7])
print(cheer[-1])

cheer="Python rules!"
print(cheer[2:7:1])
print(cheer[2:11:3])
print(cheer[-2:-11:-3])

lyrics ="happy birthday to you happy birthday to you happy birthday dear Happy birthday to you"
counts={} #pusty sªownik
words = lyrics.split(" ") #pobiera list¦ wszystkich sªów poprzez podzielenie ci¡gu w miejscach wyst¡pienia spacji
for w in words:
    w=w.lower() #zamienia na maªe litery
    if w not in counts:
        counts[w]=1
    else:
        counts[w]+=1
print(counts)

def powtórz(napis):
    return napis+napis

print(powtórz("Hello"))