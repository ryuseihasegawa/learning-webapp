for i in range(1,5):
    for j in range(i): 
        print(i,end="")
    print()
# 以下正答
# 問 4.7 パターン 1
for i in range(1, 5):
    for j in range(i):
        print(i, end="")
    print()
# 問 4.7 パターン 2
for i in range(4, 0, -1):
    for j in range(i):
        print(i, end="")
    print()