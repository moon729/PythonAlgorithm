#뮤터블 시퀀스 원소를 역순으로 정렬

from typing import Any, MutableSequence

def reverse_array(a: MutableSequence)-> None:
    n = len(a)
    for i in range(len(a)//2):
         a[i], a[n-i-1] = a[n-i-1], a[i]
    print('배열 원소 역순 정렬 완료!')



if __name__ == '__main__':
    print('배열 원소를 역순으로 정렬')
    n = int(input('원소 수 입력 : ' ))
    array = [None] * n
    for i in range(n):
        array[i] = int(input(f'x[{i}]의 값 입력 : ' ))

    reverse_array(array)
    for i in range(n):
        print(f'x[{i}] = {array[i]}')
        
