# fhand = open('romeo.txt')
# counts = {}
# for line in fhand:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0 ) + 1
#
# lst = []
# for key, val in counts.items():
#     newtup = (val, key)
#     lst.append(newtup)
#
# lst = sorted(lst, reverse=True)
#
# for val, key in lst[:10] :
#     print(key, val)

# 가장 많이 등장한 단어 top 10 출력하기

# romeo.txt
# But soft what light through yonder window breaks
# It is the east and Juliet is the sun
# Arise fair sun and kill the envious moon
# Who is already sick and pale with grief

# <결과>
# the 3
# is 3
# and 3
# sun 2
# yonder 1
# with 1
# window 1
# what 1
# through 1
# soft 1


# 리스트 []
# 튜플 (), 소괄호
# 딕셔너리 {}

fhand = open('romeo.txt')
counts = {}

for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

lst = []
for key, val in counts.items() :
    newtup = (val, key)
    lst.append(newtup)

lst.append(newtup)
lst = sorted(lst, reverse=True)

for val, key in lst[:10]:
    print(key, val)



# 리스트 컴프리헨션
# 간결하게 리스트를 만들 수 있는 방법

c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k, v in c.items() :
    tmp.append( (v, k) )

tmp = sorted(tmp)
print(tmp)

# 위와 같음.
c = {'a':10, 'b':1, 'c':22}
print( sorted( [ (v,k) for k,v in c.items() ] ) )
# [(1, 'b'), (10, 'a'), (22, 'c')]
