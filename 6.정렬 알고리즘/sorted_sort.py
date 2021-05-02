# sorted() 함수 사용해 정렬하기

num = int(input('원소 수 입력 : '))
x = [None] * num

for i in range(num):
    x[i] = int(input(f'x[{i}] : '))

#배열 x를 오름차순 정렬
x = sorted(x)
print('오름차순 정렬 완료')
for i in range(num):
    print(f'x[{i}] = {x[i]}')

#배열 x를 내림차순으로 정렬
x = sorted(x, reverse = True)
print('내림차순 정렬 완료')
for i in range(num):
    print(f'x[{i}] = {x[i]}')