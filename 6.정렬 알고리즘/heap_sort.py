# 힙 정렬 알고리즘 구현
from typing import MutableSequence

def heap_sort(a: MutableSequence) -> None:
    def down_heap(a: MutableSequence, left:int, right:int)-> None:
        temp = a[left]
        parent = left
        while parent < (right + 1) //2:
            cl = parent * 2 + 1
            cr = cl + 1
            child = cr if cr <= right and a[cr] > a[cl] else cl
            if temp >= a[child]:
                break
            a[parent] = a[child]
            parent = child
        a[parent] = temp

    n = len(a)

    # a[i] ~ a[n-1] 을 힙으로 만들기 (주어진 배열을 힙으로 만들기)
    for i in range((n-1) // 2, -1, -1):
        down_heap(a, i, n-1)

    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0] #최댓값인 a[0]와 마지막 원소 교환
        down_heap(a, 0, i - 1) #a[0] ~ a[i - 1]을 힙으로 만들기

if __name__ == '__main__':
    print('힙 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요. : '))
    x = [None] * num    # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    heap_sort(x)        # 배열 x를 힙 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')