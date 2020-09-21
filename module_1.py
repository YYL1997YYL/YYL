# import random
# def create_phone():
#     second = [3, 4, 5, 7, 8][random.randint(0, 4)]
#     third = {
#         3: random.randint(0, 9),
#         4: [5, 7, 9][random.randint(0, 2)],
#         5: [i for i in range(10) if i != 4][random.randint(0, 8)],
#         7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
#         8: random.randint(0, 9),
#     }[second]
#     suffix = random.randint(9999999,100000000)
#     return "1{}{}{}".format(second, third, suffix)
# phone = create_phone()
# print(phone)


try:
    #r = open("module_2","r")
    print(1 / 2)
except (FileNotFoundError,ZeroDivisionError) as e:
    print(e)
    print("执行程序遇到了问题")
    print("重新打开文件")
except ZeroDivisionError as e:
    print("被除数不能为0")
else:
    print("程序运行没报错")
finally:
    print("文件已经打开")