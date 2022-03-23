songs = {
    "Hello": 1,
    "Love": 5,
    "Staying Alive": 6,
    "Szampan": 3,
    "Moglo byc nic": 5
}

titles = [k for k,v in songs.items() if v == 5]
print(titles)