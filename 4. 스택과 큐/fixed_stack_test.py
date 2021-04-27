from enum import Enum
from fixed_stack import FixedStack

Menu = Enum('Menu', ['푸시', '팝', '피크', '검색', '덤프', '종료'])

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu] #menu의 값 가져와서 text형식으로 s list에 저장
    while True:
        print(*s, sep = ' ', end='') #list s 간격 주고 출력 
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)
s = FixedStack(64)

while True:
    print(f'현재 데이터 개수 : {len(s)} / {s.capacity}')
    menu = select_menu()

    if menu == Menu.푸시:
        x = int(input('데이터 입력 : '))
        try:
            s.push(x)
        except FixedStack.Full: #해당 exception발생 시 실행되는 statement
            print('stack is full')

    elif menu == Menu.팝:
        try:
            x = s.pop()
            print(f'popped data is {x}')
        except FixedStack.Empty:
            print('stack is empty')

    elif menu == Menu.피크:
        try:
            x = s.peek()
            print(f'peeked data is {x}')
        except FixedStack.Empty:
            print('stack is empty')

    elif menu == Menu.검색:
        x = int(input('검색할 값 : '))
        if x in s:
            print(f'{s.count(x)}개 포함되고, 맨 앞의 위치는 {s.find(x)}')
        else:
            print('search impossible')

    elif menu == Menu.덤프:
        s.dump()
    else:
        break
