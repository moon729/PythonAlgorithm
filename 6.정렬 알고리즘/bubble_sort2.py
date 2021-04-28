#버블 정렬 알고리즘 구현 - 알고리즘 개선 1(특정 pass의 교환 횟수 0이면 정렬 완료된 것이므로 정렬 중단)

from typing import MutableSequence

def bubble_sort(a: MutableSequence)-> None:
    """bubble sort"""
    n = len(a)
    ccnt = 0
    scnt = 0
    for i in range(n-1):
        exchng = 0 #패스에서 교환 횟수
        for j in range(n-1, i, -1):
            if a[j-1] > a[j]:
                scnt += 1
                a[j-1], a[j] = a[j], a[j-1]
                exchng += 1
            ccnt += 1
        if exchng == 0:
            break
    print(f'비교 횟수 {ccnt}')
    print(f'교환 횟수 {scnt}')

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



