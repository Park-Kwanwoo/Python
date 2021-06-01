n = input('input n : ')

# fibonaci 수열 : 앞 두개 더해서 다음 숫자
i = 1
a, b = 0, 1
while i <= int(n):
    print(a, end=' ')
    a, b = b, a + b
    i = i + 1
