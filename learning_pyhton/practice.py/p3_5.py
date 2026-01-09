num1 = int(input("1つ目の数字を入力してください："))
num2 = int(input("2つ目の数字を入力してください："))
num3 = int(input("3つ目の数字を入力してください："))

max_value = num1
if num2 > max_value:
    max_value = num2
if num3 > max_value:
    max_value = num3
print(max_value)