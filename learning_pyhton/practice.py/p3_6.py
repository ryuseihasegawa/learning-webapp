num = int(input("数字を入力してください："))

if not(num >= 0 and num <= 10):
    print("範囲外です")
elif num >= 7:
    print("合格です")
else:
    print("不合格です")