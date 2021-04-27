#배열 원소의 최댓값을 구해서 출력하기(원솟값을 난수로 생성)

import random
from max import max_of

print('난수의 최댓값 구하기')
num = int(input('난수의 개수 입력 : ' ))
min = int(input('난수의 최솟값 입력 : ' ))
max = int(input('난수의 최댓값 입력 : ' ))

x = [None] * num

for i in range(num):
    x[i] = random.randint(min, max)

print(f'{x}')
print(f'배열에서 최댓값은 {max_of(x)}임')
