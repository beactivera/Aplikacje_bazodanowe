from numpy import random
x = random.randint(100)
print(x)
jednosci = x%10
dziesiatki = int((x/10)%10)
setki = int((x/100)%10)

print("cyfra jednosci: ", jednosci)
print("cyfra dziesiatek", dziesiatki)
print("cyfra setek: ", setki)