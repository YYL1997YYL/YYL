#1、编写一个返回随机手机号的方法
import random
for _ in range(1):
  print('18' +str(random.randrange(4,10))+ ''.join( str(random.choice(range(10))) for _ in range(8) ))

  print( range )

#2、编写一个返回指定长度和内容的随机字符串方法
def generate_random_str(randomlength=10):
    random_str = ""
    base_str = "qazwsx123456"
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0,length)]
    return random_str
f = generate_random_str(24)
print (f)

import random




#3、编写一个返回随机姓名的方法