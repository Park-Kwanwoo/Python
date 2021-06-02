def fibo01(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a+b


def fibo02(n):
    list01 = list()
    a, b = 0, 1
    for i in range(n):
        list01.append(a)
        a, b = b, a + b
    return list01



if __name__=='__main__':
    n = int(input('n : '))
    # 입력된 숫자 만큼 출력
    fibo01(n)

    # 입력된 숫자 만큼 반복해서 List에 저장 후, list return
    print(fibo02(n))