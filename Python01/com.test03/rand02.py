import random as r

# 1 ~ 45, 중복되지 않는 7개 숫자
def lotto():
    res = set()
    for i in range(0, 7):
        res.add(r.randint(1, 45))
    print(res, end=' ')


if __name__=='__main__':
    lotto()