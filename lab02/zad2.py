def ispermutation(l1, l2):
    if len(l1) != len(l2):
        return False
    else:
        l1 = l1.sort()
        l2 = l2.sort()

        if l1 == l2:
            return True

l1 = [1,2,3,4]
l2 = [4,3,2,1]

print(ispermutation(l1, l2))