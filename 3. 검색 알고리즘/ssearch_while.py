#while문으로 작성한 선형 검색 알고리즘

from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 값이 같은 원소를 선형 검색"""
    i = 0
    while True:
        if i == len(a):
            return -1 #검색할 값 못 찾음
        if a[i] == key:
            return i
        i += 1


if __name__ == '__main__':
    
    n = int(input("원소 수 입력 : "))
    x = [None] * n
    
    for i in range(n):
        x[i] = int(input(f'x[{i}] : '))

    k = int(input('검색할 값을 입력하세요 : '))

    idx = seq_search(x, k)
    if idx == -1:
        print('검색하는 값이 배열에 없습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')
        
