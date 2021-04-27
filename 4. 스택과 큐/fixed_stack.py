#고정 길이의 stack class - FixedStack

from typing import Any

class FixedStack:

    class Empty(Exception):
        """비어있는 fixedstack에 팝 또는 피크할 때 내보내는 예외처리"""
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity: int=256) -> None:
        """스택 초기화"""
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def __len__(self) -> int:
        """스택에 쌓여있는 데이터 개수 리턴"""
        return self.ptr

    def is_empty(self) -> bool:
        return self.ptr <= 0 #비어있으면 true, 아니면 false 반환

    def is_full(self) -> bool:
        return self.ptr >= self.capacity

    def push(self, value:Any) -> None:
        if self.is_full():
            raise FixedStack.Full #예외 처리 발생
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self) -> Any:
        """스택에서 데이터를 피크(꼭대기 데이터 들여다보기)"""
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr - 1]

    def clear(self) -> Any:
        self.ptr = 0 #stack pointer = 0으로 하면 clear됨


    def find(self, value:Any) -> Any:
        for i in range(self.ptr-1, -1, -1):
            if self.stk[i] == value:
                return i
        return -1
    def count(self, value:Any) -> int:
        """value 개수 반환"""
        c = 0
        for i in range(self.ptr):
            if self.stk[i] == value:
                c += 1
        return c
    def __contains__(self, value:Any) -> bool:
        return self.count(value) #or value in stk 

    def dump(self) -> None:
        if self.is_empty():
            print('stack is empty')
        else:
            print(self.stk[:self.ptr]) #slice 식. list 처음부터 ptr개 출력 



















        
