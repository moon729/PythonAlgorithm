# 병합정렬 - 정렬을 마친 두 배열 병합하기

from typing import Sequence, MutableSequence

def merge_sorted_list(a: Sequence, b: Sequence, c: Sequence) -> None:
    pa, pb, pc = 0, 0, 0 # 각 배열의 커서
    na, nb, nc = len(a), len(b), len(c) # 각 배열의 원소 수

    while pa < na and pb < nb:
        if a[pa] < b[pb]:
            c[pc] = a[pa]
            pa += 1
        else:
            c[pc] = b[pb]
            pb += 1
        pc += 1
    # a에 남은 1개 원소를 c에 복사
    while pa < na:
        c[pc] = a[pa]
        pa += 1
        pc += 1
    # b에 남은 1개 원소를 c에 복사
    while pb < nb:
        c[pc] = b[pb]
        pb += 1
        pc += 1

if __name__ == '__main__':
    b = [2,4,6,8,11,13]
    a = [1,2,3,4,9,16,21]
    c = [None] * (len(a) + len(b))
    print('정렬을 마친 두 배열의 병합 수행')
    merge_sorted_list(a, b, c)

    print('배열 a, b 병합 -> c에 저장')
    print(f'배열 a : {a}')
    print(f'배열 b : {b}')
    print(f'배열 c : {c}')
