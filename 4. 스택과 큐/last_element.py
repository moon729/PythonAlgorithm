#ring buffer : 마지막 n개의 데이터만 저장

n = int(input('정수를 몇 개 저장? : '))
a = [None] * n

cnt = 0
while True:
    a[cnt % n] = int(input((f'{cnt+1}번째 정수 입력 : ')))
    cnt += 1

    retry = input(f'계속할까요?(y/n):')
    if retry in {'N', 'n'}:
        break

i = cnt - n
if i < 0: i = 0

while i < cnt:
    print(f'{i + 1}번째 = {a[i % n]}')
    i += 1
