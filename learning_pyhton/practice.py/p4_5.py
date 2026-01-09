sum : int = 0

while True:
    num = int(input("数字を入力："))
    sum  = sum + num
    if num == 0: 
        break    
print(sum)