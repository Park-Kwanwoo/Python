# tuple : list 와 거의 같다.

# 생성자 사용
a = tuple([1])
print(a)
b = tuple([1, 2, '3'])
print(b)

# tuple은 값 추가 수정 불가
# b[1] = '2'

# () 사용
d = tuple(range(3, 6))
print(a + b)
print(d)
print(b + d)

# tuple -> list
e = list(d)
e.append(6)
print(e)

# list -> tuple
f = tuple(e)
print(f)

# unpacking - iterator한 객체에서 하나하나 씩 가져온다, _로 원하지 않는 갯수 뺄수 있음, 꼭 갯수만큼 해야한다.
g, h, i, j = f
print(g)
print(h)
print(i)
print(j)

