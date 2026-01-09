mystr_a : str = input("a")
mystr_b : str = input("b")
mystr_c = mystr_a
mystr_a = mystr_b
mystr_b = mystr_c
print(f"{mystr_a+mystr_b}")