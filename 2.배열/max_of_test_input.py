from max import max_of

print('배열 최댓값 구하기')
print('주의 : End 입력 시 종료')

number = 0
x = []

while True:
    s = input(f'x[{number}]의 값 입력')
    if s == 'End':
        break
    x.append(int(s))
    number += 1

print(f'{number}개 입력함')
print(f'최댓값은 {max_of(x)}임')
