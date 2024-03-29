# 산술연산
a = 21
b = 2

print(a + b)
print(a - b)
print('---------')
print(a * b)
print(a ** b) # a^b
print('---------')
print(a / b)
print(a // b)  # 몫 (floor division - 소수점 이하는 버림)
print('---------')
print(a % b)

# 비교연산
a, b = 5, 3
print(a == b)
print(a != b)
print(a > b)
print(a <= b)
print(a is b)
print(a is not b)

print(True or True)
print(True or  False)
print(False and True)
print(False and False)
print(not False)

#  범위연산
# range(n) : 0 ~ < n
list01 = list(range(100))
print(list01)

print(list01[2])
print(list01[12:49]) # 12 ~ 48
print(list01[12:49:3]) # 3씩 증가하면서 범위 출력

# [start: end] = start ~ end-1
# [start: end: step] = start ~ end-1 까지 step만큼 증가하면서
str01 = 'Hello, World!'
print(str01[0:5])
print(str01[:5])
print(str01[7:])
print(str01[7:12])
print(str01[:4] * 3)

# reverse
print(str01[-1])
print(str01[-6:])
print(str01[:-1])
print(str01[::-1])

# 멤버연산
list02 = [0, 1, 2, 3, 4]
print(3 in list02)
print(9 in list02)
print(9 not in list02)


