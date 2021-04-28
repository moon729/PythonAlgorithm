#버블 정렬 알고리즘 구현 - 알고리즘 개선 2(특정 원소 이후 교환 일어나지 않으면, 그 원소 앞부분은 정렬 완료이므로 생략)

from typing import MutableSequence

def bubble_sort(a: MutableSequence)-> None:
    """bubble sort"""
    n = len(a)
    ccnt = 0
    scnt = 0
    k = 0 #마지막 교환 발생한 원소 저장

    while k < n - 1:
        last = n - 1
        for j in range(n-1, k, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                scnt += 1
                last = j
            ccnt += 1
        k = last

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



