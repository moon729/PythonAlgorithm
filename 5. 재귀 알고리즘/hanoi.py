#tower of hanoi

def move(no:int, from_pos:int, via:int, to_pos:int) -> None:
    if no == 1:
        print(f'원반 [{no}]을 {from_pos}->{to_pos}로 이동')
        return

    if no > 1:
        move(no - 1, from_pos,to_pos, via)

    print(f'원반[{no}]을 {from_pos} -> {to_pos}로 이동')

    if no > 1:
        move(no - 1, via,from_pos, to_pos)

n = int(input('원반 개수 입력 : '))

move(n, 1, 2, 3) 
