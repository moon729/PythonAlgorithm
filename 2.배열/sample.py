
n = int(input('짧은 변 길이 입력 : ' ))

for i in range (1, n + 1):
    print(' '*(n-i), end='')
    print('*'*i)
