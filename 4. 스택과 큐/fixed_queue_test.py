#고정 길이 큐 클래스 사용

from enum import Enum
from fixed_queue import FixedQueue

Menu = Enum('Menu', ['인큐','디큐','피크','검색','덤프','종료'])

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep=' ', end='')
        n = int(input(' : '))
        if 1 <= n <= len(Menu):
            return Menu(n)

q = FixedQueue(64)

while True:
    print(f'현재 데이터 개수 : {len(q)}/{q.capacity}')
    menu = select_menu()

    if menu == Menu.인큐:
        x = int(input('Enter data to enqueue '))
        try:
            q.enque(x)
        except FixedQueue.Full:
            print('queue is full')

    elif menu == Menu.디큐:
        try:
            x = q.deque()
            print(f'dequeued data is {x}')
        except FixedQueue.Empty:
            print('queue is empty')

    elif menu == Menu.피크:
        try:
            x = q.peek()
            print(f'peeked data is {x}')
        except FixedQueue.Empty:
            print('queue is empty')

    elif menu == Menu.검색:
        x = int(input('Enter data to search '))
        if x in q:
            print(f'{q.count(x)}개 포함, 맨 앞 위치는 {q.find(x)}')
        else:
            print('cannot find {x}')

    elif menu == Menu.덤프:
        q.dump()
    else:
        break
    
