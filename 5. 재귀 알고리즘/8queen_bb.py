#행과 열에 퀸을 1개 배치하는 조합을 재귀적으로 나열하기

pos = [0] * 8
flag = [False] * 8

def put() -> None:
    """각 열에 배치한 퀸의 위치 출력"""
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()

def set(i: int) -> None:
    """i열의 알맞은 위치에 퀸 배치"""
    for j in range(8):
        if not flag[j]: #i열 j행이 비어있을 경우
            pos[i] = j
            if i == 7: #모든 열에 퀸 배치 완료
                put()
            else:
                flag[j] = True #j행에 퀸 배치 완료
                set(i + 1) #다음 열로 넘어가기
                flag[j] = False #한번 배치 끝난 후, j행 비우기

set(0) #0열부터 퀸 배치 시작~7열까지