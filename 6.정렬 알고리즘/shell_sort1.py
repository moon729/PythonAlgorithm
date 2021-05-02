#셸 정렬 알고리즘

from typing import MutableSequence

def shell_sort(a: MutableSequence) -> None:

    n = len(a)
    h = n // 2
    while h > 0:
        for i in range(h, n):
            j = i - h
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j + h] = a[j]
                j -= h
            a[j + h] = tmp #위 while문에서 j -= h 하고 빠져나왔기 때문에 다시 원래대로 돌려줘야 함
        h //= 2

if __name__ == '__main__':
    print('셸 정렬 수행.')
    num = int(input('원소 수 입력 : '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    shell_sort(x)

    print('오름차순 정렬 완료')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
