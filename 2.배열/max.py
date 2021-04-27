#시퀀스 원소의 최댓값 출력

from typing import Sequence, Any

def max_of(a: Sequence) -> Any:
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum
