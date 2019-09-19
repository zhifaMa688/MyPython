#本程序为判断与循环语句的练习程序
#练习一：找出100-1000中的所有水仙花数（#水仙花数：每一位上的数字的3次方的和与该数相等）。
# for i in range(100, 1000):
#     a = i % 10
#     b = i // 10 % 10
#     c = i // 100
#     if i == a**3 + b**3 +c**3:
#         print(f"{i}是水仙花数！")

#练习二：找出100以内所有的质数（质数：大于1且只能被0和本身整除的数）。
# list = []
# for i in range (2, 100):
#     result = True
#     for j in range(2, i):
#         if  i % j == 0:
#             result = False
#             break
#     if result == True:
#         list.append(i)
# print(f"100以内的质数有{list}.")    

#练习三：在控制台打印出9*9乘法表
#1*1 ... 1*9
#2*1 ... 2*9
#   ...
#9*1
# for i in range (1, 10):
#     for j in range (1, 10):
#         print(f"{i}*{j}={i*j:2d}", end = "\t")
#     if j == 9:
#         print("")

