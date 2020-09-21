# # def div(c,d):
# #     if d == 0:
# #         print("被除数不能为0")
# #     else:
# #         print(c / d)
# #
# # div(90,10)
# # div(80,30)
# # div(1985,789)
# #
# # def selcet_data(sql):
# #     res = "查询"
# #     return  res
# # result = selcet_data("")
# # print(result)
# #
#
# # def s(q=10,w=10):
# #     return q+w
# # print(s(7,77))
# #
# # print(s(w=1))
# #
# # print(s(q=3))
# #
# # print(s(20,w=1))
#
# def ar(*aegs,**kwargs):
#     print(aegs)
#     print(kwargs)
#
# ar(1,4,7,8,5,6,c=1001,d=9981)
#
# b = 9981
# print(id(b))
#
# i = input("获取")
# print(i)
#
# print(type(a))
# print(type("abc"))
#
# print(isinstancl = [1,2,3,4]
# print(len(l))e("",int))
# #
# for i in range(1,10):
#     for j in range (1,i+1):
#         print(i)
#     print(l)


# def aaa():
#     global
#     c=20
#
# aaa()
# # print(c)
#
# a = "1234567890"
# b = "147258369"
#
# print(a[-2:])
# print(a[1:9])
# print(b[2:-3])
# print(a+b)
# print(a[0])
#
# a= "  325698  "
# print(a.strip())
# print(a)
# print(a.lstrip())
# print(a.rstrip())
#
# line = "账户，金额，取款，余额"
# line = line.replace(",",",")
# print(line)
# print(line.split(','))

























# for i in range(1,10):
#      for j in  range(1,i+1):
#         print("%dx%d=%2d"%(j,i,j*i),end=' ')
#      print("")
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{}x{}={}".format(j,i,i*j),end='\t')
# #     print()
#
# l=[1,2,3,4,5,6,7,8,9]
# # for i in l:
# #     print(i)
# l[0]=20
# # l.append(9)
# l.extend((1,2,3,4,5,6))
# l.pop(0)
# print(l)
#
#
# def bubbleSort(arr):
#     n = len(arr)
#
#     # 遍历所有数组元素
#     for i in range(n):
#
#         # Last i elements are already in place
#         for j in range(0, n - i - 1):
#
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
#
# arr = [64, 34, 25, 12, 22, 11, 90]
#
# bubbleSort(arr)
#
# print("排序后的数组:")
# for i in range(len(arr)):
#     print("%d" % arr[i]),
#
# a = [64, 34, 25, 12, 22, 11, 90]


l = [10,1,35,61,89,36,55]
for i in range(len(l)-1,0,-1):
    for j in range(0,i):
        if(l[j] > l[j+1]):
            l[j],l[j+1]=l[j+1],l[j]
print(l)


# def s(a=1,b=10):
#      return a+b
#  print(s(1,3))

class str_demo():

#     s = None
#
#     def replace(self):
#         print("字符串替换")
#
#     def split(self):
#         print("字符串切割")
#
# sd = str_demo()
# sd.s = "who are you"
# sd.replace()
# sd.split()
#
# def __init__(self):
#     print("魔法方法")
#
# def replace(self):
#     print("实例方法")
#     pass
#
# @classmethod
# def split(cls):
#     print("类方法")
#
# @staticmethod
# def  static():
#     print("静态方法")
#
# def s(a,b):
#     return a+b
# print(s(11,2))
#
# a = "  sdfsdfsdfs   "
# print(a.rstrip())
#
# a = "小明,小红,张"
# print(a.split(","))
#
# a = "小明,小红.张"
# a = a.replace(".",",")
# print(a)

# a = "小明,小红.张"
#
# print(a.find("."))

class PrivateDemo():
    _a = None

    def set__a(self,value):
        self.__a = value
    def get__a(self):
        return self.__a
p = PrivateDemo()
p.set__a("hello")
print(p.get__a())
print(p.__a)