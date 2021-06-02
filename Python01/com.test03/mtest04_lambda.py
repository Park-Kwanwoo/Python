# lambda 필요할 때마다 간단하게 쓰는 '익명' 함수
# None = null 같은 의미
hap01 = lambda a, b: a + b
print(hap01(10, 20))

hap02 = lambda a, b, c: a + b + c
print(hap02(30, 40, 50))

gob = lambda a, b : a * b
print(gob(12,34))

a = [(1, 'one', 9), (2, 'two', 8), (3, 'three', 7), (4, 'four', 6)]
print(a)
a.sort(key=lambda a: a[2])
print(a)
# 참 if 조건 거짓
min01 = lambda x, y: x if x < y else y
# min01 = (lambda x, y: x if x < y else y)(3, 4)
print(min01(1, 3))

max01 = lambda x, y: x if x > y else y
print(max01(5, 3))

b = lambda x: (lambda newx: x + newx)
print(b(100)(200))
c = b(100)
# c = lambda newx: 100 + newx
d = c(200)
print(d)

# 1 ~ 100 사이의 5의 배수 출력
e = lambda x: bool(x % 5)
five = [i for i in range(1, 101) if not e(i) ]
print(five)

f = lambda x: x if (x % 5 != 0) else None
res = [i for i in range(1, 101) if not f(i)]
print(res)

result = [i for i in range(1, 101) if not (lambda x: x if (x % 5 != 0) else None)(i)]
print(result)
