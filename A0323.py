'''
변수명 정하기
1) 영문과 숫자, _로 이루어진다.
2) 문자나 _로 시작한다
3) 특수문자를 사용하면 안된다.(&,%등)
4) 키워드 사용하면 안된다.(if ,for등)
5) 대소문자를 구분한다

'''
from builtins import print
'''
a=1
b=2
A=3
print(a,b,A)

a,b,c=3,2,1

print(a,b,c)

# 값 교환
a,b=10,20
print(a,b)

a,b=b,a
print(a,b)

a=123
print(type(a))

a=123.45
print(type(a))

a='hani'
print(type(a))

print("num")
a,b,c=1,2,3
print(a,b,c)
print("num :",a,b,c)

print(a,b,c,sep=',')
print(a,b,c,sep='')
print(a,b,c,sep='\n')

# 나란히 출력하고 싶을 때
print(a,end=' ')
print(b,end=' ')
print(c)

str="hani"
print(str[-3])
print(len(str))

# 0~2까지 [0],[1],[2]
print(str[0:3])
# 0부터 끝까지
print(str[0:])

print(str[0:4])

# d=>정수
a="I eat %f apples" %3.0
print(a)

b="I eat %s apples" %"five"
print(b)

c="I eat {0} apples" .format(3)
print(c)

c="I eat {0} apples" .format("five")
print(c)

d="내 이름은 {0}이고 과목은 {1}를 좋아 하며 " \
  "{2}시에 일어 납니다." .format('종진','파이썬',6)
print(d)

e="I need python"
print(len(e))





msg="It is Computer"
print(msg.upper())
print(msg.lower())
print(msg)

tmp=msg.upper()
print(tmp)

print(tmp.find("C"))
print(msg.count("C"))
print(tmp.count("I"))
print(msg[:2])
print(msg[3:])
print(msg[3:5])
print(len(msg))


num=3
day="seven"

str1="%d번 밥을 먹고 %s일 동안 쉬었다"%(num,day)
print(str1)

str2="{0}번 밥을 먹고 {1}일 동안 쉬었다".format(num,day)
print(str2)

p="801013-1032132"
print(p[:6])
print(p[7:])

# split 함수는 a.split()처럼 괄호 안에 아무 값도 넣어 주지 않으면
# 공백(스페이스, 탭, 엔터 등)을 기준으로 문자열을 나누어 준다.
a="Life is too short"
print(a.split())

b="a:b:c:d"
print(b.split(":"))



# input => 입력함수
a=input("숫자를 입력하세요 : ")
print(a)

a1,b1=input("숫자를 입력하세용 : ").split()
print(a1,b1)
print(type(a1))
c=a1+b1
# type 이 str 즉, 문자열이기 때문에 a1+b1은
# 나열연산이 되어버린다
print(c)
print(type(c))
a,b=input("숫자를 입력하세요 : ").split()
a=int(a)
b=int(b)
print(a+b)
print(type(a))


a=4.3
b=4
c=a+b
print(type(c))

# 반복함수 map
a,b=map(int, input("숫자를 입력하세요 : ").split())
print(a+b)
print(a-b)
print(a**b)
print(a%b)
print(a//b)

a="i eat {0} apples".format(3)
print(a)

a = f"i eat {4} apples"
print(a)

# 파이썬 자료구조 : 리스트[] , 셋(set), 딕셔너리(key, value)
odd=[1,3,5,7,9]
print(odd)

print(odd[0])
print(odd[1])
print(odd[0:4])
print(len(odd))
odd[0]=10
print(odd)


a=[]
print(a)

b=list()
print(b)
# a와 b의 구조가 똑같이 나온다(비어있는 list 구조)

'''
'''
a=[1,2,3,4,5]
print(a[0]+a[4])

b=list(range(1,11))
print(b)

c=a+b # 리스트 + 리스트 = 리스트 나열
print(c)

# append list에 요소 추가 함수
a.append(6)
print(a)

# insert 위치 선정하여 삽입
a.insert(3,7)
print(a)

height,kg=map(float,input("키와 몸무게 입력 : ").split())

str=f"키는 {height}이고, 몸무게는 {kg}입니다."

print(str)


# pop 맨 마지막(끝 값)요소 값이 삭제
a.pop()
print(a)

# pop 값을 주면 안에 있는 index의 요소를 삭제
a.pop(3)
print(a)

# remove 는 실제 안에 들어 있는 값이 삭제
a.remove(4)
print(a)

# '3'의 인덱스 위치를 찾음
print(a.index(3))

a=list(range(1,11,2))
print(sum(a))
print(max(a))
print(min(a))
print(min(7,2))
print(max(1,7,2))


li=[3,4,5]
li[0]=10
print(li)

# 튜플은 값을 수정(삭제)할 수 없다
tu=(3,4,5)
#tu[0]=10
# del tu[0]
print(tu)

invite=["종진","신요","형민"]
invite.append("승주")
print(invite)

invite.insert(2,"건상")
print(invite)

invite.pop(0)
print(invite)

invite.remove("신요")
print(invite)

import random as r

a=list(range(1,11))

r.shuffle(a)
print(a)
# 정렬함수(sort=오름차순)
a.sort()
print(a)
# 역순(reverse=True)
a.sort(reverse=True)
print(a)

a.clear()
print(a)
'''
# sep = 구분자
# input = 입력함수
# map = 반복함수
#




