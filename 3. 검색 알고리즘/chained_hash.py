#체인법으로 해시 함수 구하기

from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    """해시를 구성하는 노드"""

    def __init__(self, key:Any, value:Any, next:Node) -> None:
        """초기화"""
        self.key = key
        self.value = value
        self.next = next #뒤쪽 노드를 참조 

class ChainedHash:
    """체인법으로 해시 클래스 구현"""

    def __init__(self, capacity:int) -> None:
        self.capacity = capacity #해시 테이블의 크기 지정
        self.table = [None] * self.capacity #해시 테이블(리스트) 선언

    def hash_value(self, key:Any) -> int:
        """해시값을 구함"""
        if isinstance(key, int): #key의 자료형 확인 내장함수 
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)


    def search(self, key:Any) -> Any:
        """키가 key인 원소를 검색해 값 반환"""
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return p.value #키, 해시 일치하는 노드 검색 성공
            p = p.next #다음 노드 주목
        return None #검색 실패 

    def add(self, key: Any, value: Any) -> bool:
        """키가 key이고 값이 value인 원소를 삽입"""
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return False #삽입 실패 
            p = p.next
            
        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
        return True #삽입 성공 
        

    def remove(self, key:Any) -> bool:
        """키가 key인 원소를 삭제"""
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None #바로 앞 주목 노드

        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True
            pp = p
            p = p.next #뒤쪽 노드를 주목하며 반복문 수행
        return False #삭제 실패 

    def dump(self) -> None:
        """해시 테이블을 덤프"""
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f' -> {p.key} ({p.value})', end='') #해시 테이블에 있는 키와 값을 출력
                p = p.next
            print()
