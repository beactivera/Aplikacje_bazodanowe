napis="ala ma kotA"
print(napis)

# ----
x = 1
if x < 100:
    print("pierwszy warunek\nzostał spełniony")
else:
    print("drugi warunek\nzostał spełniony")

# ----
x = 1
y = 3
if x < 100:
    print("został spełniony")
    if y % 3 == 0:
        print("pierwszy i drugi warunek")
    else:
        print("tylko pierwszy warunek")
else:
    print("pierwszy warunek\nnie został spełniony")