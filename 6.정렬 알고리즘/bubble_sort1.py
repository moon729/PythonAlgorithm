#버블 정렬 알고리즘 구현

from typing import MutableSequence

def bubble_sort(a: MutableSequence)-> None:
    """bubble sort"""
    n = len(a)
    for i in range(n-1):
        for j in range(n-1, i, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]


if __name__ == '__main__':
    print('bubble sort')
    num = int(input('원소 수 입력 : '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]:'))

    bubble_sort(x)

    print('오름차순 정렬 완료.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')



