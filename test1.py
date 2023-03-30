
# 1. 입력으로 1 개의 정수   N이 주어진다. 정수 N의 약수를 오름차순으로 출력해라.
# ex) 입력 : 10        출력: 1 2 5 10
#
n=int(input('정수 입력 :'))
list1=list()
for x in range(1,n+1) :
    if(n%x==0):
        list1.append(x)
list1.sort()
print(list1)

# 2. 10개의 수를 입력 받아, 그 중에서 가장 큰 수를 출력하는 프로그램을 작성하라.
# ex) 3                                 출력:
#    3 17 1 39 40 41 2 33 100 2                 1  100
#    22 8 5 134 9 4 28 3 4 29                   2  134
#    6 63 2 6 89 84 32 43 2 1                   3  89
#
# 1번방법( 띄어쓰기로 10번 한꺼번에 입력 )
num1= list(map(int, input("10개의 정수를 입력 : ").split()))
print(max(num1))

# 2번방법(입력가능 횟수를 10번으로 제한)
num2=list()
for i in range(10):
    a = int(input("정수입력 : "))
    num2.append(a)

print(num2)
print(max(num2))

# 3. 아래와 같은 모양 출력해라.  (for문 중첩)
#   &++++ a=0
#   +&+++ a=1
#   ++&++ a=2
#   +++&+ a=3
#   ++++& a=4
#
a="&"
b="+"
for i in range(5):
    if i==1:
        continue
    for j in range(5):
        if j==i and i!=1:
           print(a,end="")
        else:
            print(b,end="")

    print()

# 4. num이라는 리스트에 1부터 10까지 준 후, filter()함수, list함수, lambda식을 이용해서 홀수, 5보다 큰값을 출력.
#

num=list(filter(lambda x : x%2!=0 and x>5,range(1,11)))
print(num)
# 5. 문자와 숫자가 섞인 문자열을 입력받을 때 구별하여 출력해라.
# input: abc23 1de
# output:
#

str1=list(input("입력!"))
ord1=list(map(int,map(ord,str1)))
a="숫자 :"
b="문자 :"
num=list()
str2=list()
for i in range(len(ord1)):

    if ord1[i]>47 and ord1[i]<58 :
        num.append(str1[i])
        a+=str1[i]
    else:
        str2.append(str1[i])
        b+=str1[i]

print("문자 : ",str2,end="")
print("숫자 : ",num)
print(a,b)
# 강사님 풀이
str1=input()
li=list(str1) #['a','b' c '2' 3 1de
num=['1','2','3','4','5','6','7','8','9','0']
n=""  #숫자
s=""  #문자
for i in li:
    if i in num:
        n=n+i
    else:
        s=s+i
print("문자 : {0} 정수:{1}".format(s,n))
# 준형이 풀이
data = input("문자와 숫자로 구성된 문자열을 입력하세요: ")
letters = ""
numbers = ""

for char in data:
    try:
        int(char)
        numbers += char
    except ValueError:
        letters += char

print("문자: " + letters)
print("정수: " + numbers)
# 6. $$$$ 이러한 모양 출력해라.
# $$$$
#
for i in range(2):
    for j in range(4):
        print("$",end="")
    print()

# 7. 숫자를 입력받으면 그에 해당하는 자리수를 출력
# 입력: 330 출력; 100의 자리수
# 입력: 19203 출력: 10000의 자리수
num= len(input("정수 입력 : "))
x="1"
for i in range(num-1):
    x+="0"
print(x,"의 자리 숫자")


# p.112~115
# Q1.
국어=80
영어=75
수학=55
def ave():
  return (국어+영어+수학)/3
print("홍길동씨의 평균 점수 : ",ave())
# Q2
# 13%2==0 : 짝수
# 13%2!=0 : 홀수

# Q3
pin="881120-1068234"
a=pin.split("-")
yyyymmdd=a[0]
num=a[1]
print("yyyymmdd : ",yyyymmdd)
print("num : ",num)
# Q4
pin="881120-1068234"
print(pin[7])

def gender():
    if pin[7]=="1" or "3":
        print("남자")
    else:
        print("여자")
gender()

# Q5
a="a:b:c:d"
b=a.replace(":","#")
print(b)

# Q6
a=[1,3,5,4,2]
a.sort()
a.sort(reverse=True)
print(a)
# Q7
a=["Life","is","too","short"]
result =" ".join(a)
print(result)

# Q8
a=(1,2,3)
a=a+(4,)
print(a)

a=(1,2,3)
lia=list(a)
lia.append(4)
a=tuple(lia)
print(a)

# Q9
# list는 값이 변할 수 있기때문에 key의 값으로 쓸 수 없다.
# 반면 튜플은 변경이 불가능 하기때문에 key로 사용이 가능!
# 3번

# Q10
a={'A':90,'B':80,'C':70}
# result=a.get('B')
result=a.pop('B')
print(a)
print(result)

# Q11
a=[1,1,1,2,2,3,3,3,4,4,5]
aSet=set(a)
b=list(aSet)
print(b)

# Q12
a = b = [1,2,3]
a[1] = 4
print(b)
# 메모리의 주소값을 복사
# 같은 값을 가짐
# b가 참조하는 주소는 a의 주소이기 때문에
# a의 값이 변경이 되면 b의 값도 변경이 됨
a1=[1,2,3]
b1=a1.copy()
a1[1]=4
print(b1)
# 복제 : 다른 메모리의 주소값을 가짐
# a가 변경이 되어도 b는 변경이 되지 않음

# 복제하는 방법

# 1.객체 선언 후 슬라이싱
li1 = [1,2,3]
li2 = li1[:]
print(id(li1),id(li2))
# 2.list() 사용
li1 = [1,2,3]
li2 = list(li1)
print(id(li1),id(li2))
# copy() 사용
li1 = [1,2,3]
li2 = li1.copy()
print(id(li1),id(li2))
# list 연산
li1 = [1,2,3]
li2 = [] + li1
print(id(li1),id(li2))

# p.146~148
# Q1
a = "Life is too short, you need python"
if "wife" in a : print("wife")
elif "python" in a and "you" not in a : print("python")
elif "shirt" not in a : print("shirt")
elif "need" in a : print("need")
else: print("none")
# 정답 : "shirt"

# Q2
result = 0
i = 1
while i <= 1000 :
    if i%3==0 :
        result += i
    i += 1
print(result)

# Q3
i = 0
a ='*'
while True:
    i += 1
    if i > 5:
        break
    print(a*i)
# Q4
for i in range(1,101):
    print(i,end=" ")
print()
# Q5
A = [70,60,55,75,95,90,80,80,85,100]
total = 0
for score in A :
    total += score
average = total/len(A)
print(average)

# Q6

numbers = [1,2,3,4,5]

result =[]
for n in numbers:
    if n % 2 == 1 :
        result.append(n*2)
    # n이 홀수면 n*2 해서 list result에 추가

result = [n*2 for n in numbers if n%2==1]
print(result)

