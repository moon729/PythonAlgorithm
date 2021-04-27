#고정 길이 queue class : FixedQueue
from typing import Any

class FixedQueue:

    class Empty(Exception):
        pass #exception 발생해도 계속 코드 진행 
    class Full(Exception):
        pass

    def __init__(self, capacity : int) -> None:
        self.no = 0 #number of data
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.queue = [None] * capacity

    def __len__(self) -> int: #함수 이렇게 선언시 len(Menu)이렇게 사용 가능 
        return self.no
    def is_empty(self) -> bool:
        return self.no <= 0
    def is_full(self) -> bool:
        return self.no >= self.capacity

    def enque(self, x:Any) -> None:
        """enqueue data x"""
        if self.is_full():
            raise FixedQueue.Full
        self.que[self.rear] = x
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0 #가장 큰 인덱스 이후 > 다시 0으로

    def deque(self) -> Any:
        """dequeue data"""
        if self.is_empty():
            raise FixedQueue.Empty
        x = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x

    def peek(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty
        return self.que[self.front]

    def find(self, value:Any) -> Any:
        """find value, return it"""
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                return idx
        return -1

    def count(self, value:Any) -> bool:
        c = 0
        for i in range(self.no):
            idx = (i + self.front) % capacity
            if self.que[idx] == value:
                c += 1
        return c

    def __contains__(self, value:Any) -> bool:
        return self.count(value)

    def clear(self) -> None:
        self.no = self.front = self.rear = 0

    def dump(self) -> None:
        if self.is_empty():
            print('queue is empty')
        else:
            for i in range(self.no):
                pritn(self.que[(i + self.front) % self.capacity],end=' ')
            print()

