# math 라는 module 사용하겠다
# import math
# math module에서 pi만 사용하겠다
from math import pi

def circle(x):
    return pi * x * x


if __name__=="__main__":
    r = input('반지름 : ')
    print('반지름이 %s인 원의 넓이는 %f 이다'%(r, circle(int(r))))
