max_value = 0

for _ in range(6):
    num = int(input("数字："))
    if max_value < num:
        max_value = num
print(max_value)