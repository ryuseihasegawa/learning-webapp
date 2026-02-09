import math

a = int(input("1 つ目の自然数を入力: "))
b = int(input("2 つ目の自然数を入力: "))
gcd = math.gcd(a, b)
print(f"最大公約数: {gcd}")