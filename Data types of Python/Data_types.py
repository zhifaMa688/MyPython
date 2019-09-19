#Python 的数据类型
a = input ("请输入一个整数：")
print (type(a))

a = int(a)
print (type(a))

if a < 5 :
    print("a小于5")
elif a == 5 :
    print("a等于5")
else:
    print("a大于5")

l = list (range(1,100,2))
print (f"list的类型是{type(l)}\n{l}")