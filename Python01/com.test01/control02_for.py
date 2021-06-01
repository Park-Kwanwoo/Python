subject = ['java', 'javascript', 'python']

for s in subject:
    print(s, end=' ')
else:
    print('재밌다.')

for i in range(1, 100):
    print(i, end=' ')

print('구구단')
for j in range(1, 10):
    print('<<' + str(j) + '>> 단')
    for i in range(2, 10):
        #print(str(i) + '*' + str(j) + '=' + str(i*j) + '    ', end=' ')
        print(i, '*' , j, '=', j*i, sep=' ')
    #print('\n')

# range 함수로 10 ~ 1 거꾸로 출력

for i in range(10, 0, -1):
    print(i , end=' ')