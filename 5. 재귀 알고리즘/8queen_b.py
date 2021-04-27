#각 열에 퀸을 1개 배치하는 조합을 재귀적으로 나열

pos = [0] * 8

def put() -> None:
    """각 열에 배치한 퀸의 위치 출력"""
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()

def set(i: int) -> None:
    """i열에 퀸을 배치"""
    for j in range(8):
        pos[i] = j #퀸을 j행에 배치
        if i == 7:
            put() #모든 열에 퀸 배치 완료시 출력
        else:
            set(i + 1)

set(0) #0열부터 퀸 배치 시작~7열까지