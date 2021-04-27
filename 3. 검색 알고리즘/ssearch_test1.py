#seq_search()로 실수 검색하기 

from ssearch_while import seq_search

print('실수 검색하기. "End"입력 시 종료')

number = 0
x = []

while True:
    s = input(f'x[{number}]:')
    if s == 'End':
        break
    x.append(float(s))
    number += 1

ky = float(input('검색할 값 입력'))

idx = seq_search(x, ky)

if idx == -1:
    print('검색 원소 존재하지 않음')
else:
    print(f'검색값은 x[{idx}]에 있음')
