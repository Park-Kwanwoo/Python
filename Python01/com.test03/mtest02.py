def fun01(x, y):
    return x+y

def fun02(x, y):
    return x+y, x-y

def fun03(x, y):
    print('{}, {} 두 개가 입력'.format(x,y))
    print('%d + %d = %d'%(x, y, x+y))

if __name__ == '__main__':
    print(fun01(3,5))
    print(fun02(3,5))
    fun03(6, 5)