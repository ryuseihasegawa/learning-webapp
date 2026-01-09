num1 = int(input("数1:"))
num2 = int(input("数2:"))
num3 = int(input("数3:"))

mylist : list =[]
mylist.append(num1)
mylist.append(num2)
mylist.append(num3)

print(f"最大値:{max(mylist)}")
print(f"最小値:{min(mylist)}")
print(f"平均値:{int(sum(mylist)/len(mylist))}")