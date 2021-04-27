#선형 알고리즘- 보초법으로 개선 

from typing import Any, Sequence
import copy

def seq_search(seq: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 값이 같은 원소를 선형 검색"""

    a = copy.deepcopy(seq)
    a.append(key)
    i = 0
    while True:
        if a[i] == key:
            break
        i += 1
    return -1 if i == len(seq) else i


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
        
