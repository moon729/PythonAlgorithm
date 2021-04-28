#셰이커 정렬 알고리즘
from typing import MutableSequence

def shaker_sort(a: MutableSequence)-> None:
    """bubble sort"""
    ccnt = 0
    scnt = 0
    left = 0
    right = len(a) - 1
    last = right

    while left < right:
        for j in range(right, left, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                scnt += 1
                last = j
            left = last
            ccnt += 1

        for j in range(left, right):
            if a[j] > a[j+1]:
                a[j+1], a[j] = a[j], a[j+1]
                scnt += 1
                last = j
            right = last


    print(f'비교 횟수 {ccnt}')
    print(f'교환 횟수 {scnt}')

if __name__ == '__main__':

    num = int(input('원소 수 입력 : '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]:'))

    shaker_sort(x)

    print('오름차순 정렬 완료.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')



