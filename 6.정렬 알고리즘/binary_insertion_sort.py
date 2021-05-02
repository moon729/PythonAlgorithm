#이진 삽입 정렬 알고리즘 구하기

from typing import MutableSequence

def binary_insertion_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(1, n):
        key = a[i]
        pl = 0
        pr = i - 1

        while True:
            pc = (pl + pr) // 2
            if a[pc] == key:
                break
            elif a[pc] < key:
                pl = pc + 1
            else:
                pr = pc - 1
            if pl > pr: break

        pd = pc + 1 if pl <= pr else pr + 1 #삽입해야 할 위치의 인덱스

        for j in range(i, pd, -1):
            a[j] = a[j-1]
        a[pd] = key

if __name__ == '__main__':
    print('이진 삽입 정렬 수행')
    num = int(input('원소 수 입력 : '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}] :'))

    binary_insertion_sort(x)

    print('오름차순 정렬 완료.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
