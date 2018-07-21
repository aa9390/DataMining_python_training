# fhand = open('Hamlet.txt')
# for line in fhand:
#     line = line.rstrip()
#     if line.startswith('im'):
#         print(line)
#
#
# fname = input('Enter the file name:  ')
# try:
#     fhand = open(fname)
# except:
#     print('File cannot be opened: ', fname)
#     quit()
#
# count = 0
# for line in fhand:
#     line= line.rstrip()
#     if line.startswith('im') :
#         count = count + 1
#
#         print(line)
# print('There were', count, 'subject lines in', fname)
#
#
# # -------------------------------------------------------------
# friends = ['Joseph', 'Glenn', 'Sally']
# carryon = ['socks', 'shirt', 'perfume']
# colors = ['red', ['yellow', 'blue'], 'black']
# emptyLIst = []
# print(colors[0])


# -------------------------------------------------
#<실습> 딕셔너리를 활용한 데이터 빈도수 측정

# <clown.txt>
# the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car

# <결과>
# Enter File: clown.txt
# the 7
# clown 2
# ran 2
# after 1
# car 3
# and 3
# into 1
# tent 2
# fell 1
# down 1
# on 1
# Done the 7

fname = input('Enter File: ')

# 파일의 길이가 1보다 작으면 파일 이름은 clown.txt로 고정
if len(fname) < 1 : fname = 'clown.txt'
# 파일에 대한 handle 선언
hand = open(fname)

# 빈 딕셔너리 생성
di = dict()
for lin in hand :
    lin = lin.rstrip() # 출력 시 개행문자 없도록
    wds = lin.split() # 빈칸으로 나눈 배열 (['the'], ['clown'],['ran'], ...)
    for w in wds :
        di[w] = di.get(w,0) + 1 # 값이 있으면 value 값을 1씩증가.
                                # {'the':7, 'clown':2, ... }

# 비교를 위해 제일 큰 값을 -1로 설정
largest = -1
theword = None
for k, v in di.items() :
    print(k,v)
    if v > largest :
        largest = v
        theword = k

print('Done', theword, largest)
