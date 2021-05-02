#셸 정렬 알고리즘 - h*3+1의 수열 사용

from typing import MutableSequence

def shell_sort(a: MutableSequence) -> None:

    n = len(a)
    h = 1

    while h < n // 9:
        h = h * 3 + 1 #n//9보단 크지 않은 상태에서 해당 수열 사용 (효울성 증가)

    while h > 0:
        for i in range(h, n):
            j = i - h
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j + h] = a[j]
                j -= h
            a[j + h] = tmp
        h //= 3

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
