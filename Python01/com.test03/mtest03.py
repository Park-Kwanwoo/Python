"""
1. for문을 사용하여 구구단 전체를 출력하는 gugu() 함수
2. while 문을 사용하여 함수 호출 시 입력된 단만 출력 gugudan(x)
3. main 함수에서 gugu(), gugudan(x) 함수 호출, gugudan 에 입력해주는 숫자는 input
"""

def gugu():
    for i in range(2, 10):
        for j in range(1, 10):
            print(str(i), '*', str(j), '=', str(i*j))


def gugudan(x):
    i = 1
    while i < 10:
        print(str(x), '*', str(i), '=', str(i*x))
        i = i + 1


if __name__=='__main__':
    gugu()
    x = input('출력할 단 : ')
    gugudan(int(x))
