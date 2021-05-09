# 도수 정렬 알고리즘 구현

from typing import MutableSequence

def fsort(a: MutableSequence, max: int) -> None:
    n = len(a)
    f = [0] * (max + 1) #누적 도수 분포표 배열 f
    b = [0] * n #작업용 배열 b

    for i in range(n): # a의 도수분포표 배열 f
        f[a[i]] += 1
    for i in range(1, max + 1): # f 의 누적 도수 분표포 값 저장
        f[i] += f[i -1]
    for i in range(n-1, -1, -1): # 작업용 배열 b
        f[a[i]] -= 1
        b[f[a[i]]] = a[i]
    for i in range(n) : #b의 값을 a에 저장
        a[i] = b[i]

def counting_sort(a:MutableSequence) -> None:
    fsort(a, max(a))

if __name__ == '__main__':
    print('도수 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요. : '))
    x = [None] * num    # 원소 수가 num인 배열을 생성

    for i in range(num):
        while True:
            x[i] = int(input(f'x[{i}] : '))
            if x[i] >= 0: break

    counting_sort(x)        # 배열 x를 힙 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')