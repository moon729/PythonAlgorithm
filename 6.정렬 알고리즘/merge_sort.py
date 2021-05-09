# 병합 정렬 알고리즘 구현

from typing import MutableSequence

def merge_sort(a: MutableSequence) -> None:
    """병합 정렬"""
    def _merge_sort(a: MutableSequence, left: int, right: int) -> None:
        """a[left] ~ a[right] 를 재귀적으로 병합 정렬"""
        if left < right:
            center = (left + right) // 2
            _merge_sort(a, left, center)
            _merge_sort(a, center +1, right)

            p = j = 0
            i = k = left

            while i <= center:
                buff[p] = a[i]
                p += 1
                i += 1
            while i <= right and j < p:
                if buff[j] <=  a[i]:
                    a[k] = buff[j]
                    j += 1
                else:
                    a[k] = a[i]
                    i += 1
                k += 1
            while j < p:
                a[k] = buff[j] #buff에 남은 원소 a에 저장
                k += 1
                j += 1

    #_merge_sort 종료, 병합 수행
    n = len(a)
    buff = [None] * n
    _merge_sort(a, 0, n - 1)
    del buff # 작업용 배열 소멸

if __name__ == '__main__':
    print('병합 정렬 수행')
    n = int(input('원소 개수 입력 : '))
    x = [None] * n

    for i in range(n):
        x[i] = int(input(f'x[{i}] : '))
    merge_sort(x)

    print('오름차순 정렬 완료')
    for i in range(n):
        print(f'x[{i}] = {x[i]}')

