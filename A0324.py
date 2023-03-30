'''

# 딕셔너리
a = {'name':'aa'}
a['subject'] = 'python'
print(a)

print(a['name'])
# keys = 키값들만 모두 출력하는 함수
print(a.keys())
# values = 값들만 모두 출력하는 함수
print(a.values())
# items = key와 value 모두 확인
print(a.items())
# in = 해당 key값이 있는지 없는지 확인할 수 있는 함수 (true,false)
print('name' in a)
# get = 해당 키값에 대한 벨류값이 반환
print(a.get('name'))
# //////////////////////////////////////////////
# 집합 자료형 ( Set)
# 1. 중복 불가능 , 2.  순서가 없다(p.112~p.115문제)
# ////////////////////////////////////////////
# if문
a,b=map(int,input("두 정수 입력 :").split())

if a > b :
    print(">")
elif a < b :
    print("<")
else:
    print("=")

for i in range(1,10,2):
    print(i)
#
x=input("정수 입력 :")
sum=0
for i in range(1,int(x)):
    if i%2==0:
        print(i)
        sum=sum+i
    else:sum=sum+i
print("합계 :",sum)
# 입력 받은 정수의 약수 출력
x=int(input('정수 입력 :'))

for i in range(1,x+1):
    if(x%i==0):
        print(i)

while True:
 a,b=map(int,input("a,b 입력 : ").split())
 if a == 0 and b==0:
  break
 print(a+b)

# int() 정수형으로 바꾸는 함수
# str() 문자열로 바꾸는 함수
# float() 소수로 바꾸는 함수

age=31
message="Happy"+str(age)+"BirthDay"
print(message)

dic = {'name': 'tom', 'age': '11'}
print(dic['name'])

dic['pro'] = 'python'
print(dic)

del dic['name']
print(dic)

s1 = set([1, 2, 3])
print(s1)

s2 = list('python')
print(s2)

# 집합(중복불가, 순서x)
s3 = set([4, 5, 6])
l3 = list(s3)
print(l3[0])
# print(s3[0])
# => list가 아닌 set(집합)은 순서가 없기 때문에 출력이 되지 않는다
# 인덱싱으로 값을 얻을 수 없음

s4=set([1,2,3,4,5])
s5=set([6,7,3,4,10])

# 교집합 ( & , intersection )
print(s4&s5)
print(s4.intersection(s5))
# 합집합 ( | , union )
print(s4|s5)
print(s4.union(s5))
# 차집합 ( - , difference )
print(s4-s5)
print(s4.difference(s5))

cm=float(input("너의 키는 ?"))
print("나의 키는 {0} cm야".format(cm))
print("나의 키는 %.1f cm 이다."%cm)

# 비어있는 딕셔너리
response={}

active=True

while active:
    name=input("너의 이름은?")
    res=input("너는 건용이를 좋아하니?")
    response[name]=res

    repeat=input("양보가능하니?")
    if repeat=='no' or '아니':
        active=False

for i,j in response.items():
    print(i+" "+j)


msg="It is Time"

for i in range(len(msg)):
    print(msg[i])

# 대문자만
for x in msg:
    if x.isupper():
        print(x,end='')
# 소문자만
for x in msg:
    if x.islower():
        print(x,end='')
# 알파벳만
for x in msg:
    if x.isalpha():
        print(x,end='')
print()

# 아스키넘버로 출력
tmp='AZ'
for x in tmp:
    print(ord(x))

# 아스키넘버를 char로 변환
tmp=65
print(chr(tmp))

a=[]
for i in range(3,31):
    if i%3==0:
        a.append(i)
print(a)

# for 앞에 변수명을 주어야함
q=[y for y in range(3,31) if i%3==0]
print(q)

li3=[i for i in range(1,11)]
print(li3)

a=[23,12,34,53,19]
print(a[:3])

for x in enumerate(a):
    print(x)
    print(x[0],x[1])


b=(1,2,3,4,5)
print(b[1])

for index, value in enumerate(a):
    print(index, value)
    print()


if all(50>x for x in a):
    print("yes")
else:
    print("no")

if any(15>x for x in a):
    print("yes")
else:
    print("no")
a=[[0]*3 for _ in range(3)]
print(a)

a[0][1]=1
a[1][1]=2

for x in a:
    print(x)

for x in a:
    for y in x:
        print(y,end=',')
    print()

for x in range(2,10):
    for y in range(1,10):
        print(x,"x",y,"=",x*y)
    print()
# 오후
def add(a,b):
    c=a+b
    d=a-b
    return c,d
a=add(3,2)
b=add(5,7)
print(a,b)



def isPrime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True
a=[12,13,7,9,19]
for y in a:
    if isPrime(y):
        print(y,end=" ")

def calcu(who,hour,num,price):
    msg="Nooooo"
    if(hour==15) and (num>=3):
        price*=0.9
        msg="10%"
    elif(hour==12) and (num>=5):
        price*=0.8
        msg="20%"
    price=int(price)
    print(f"{who}씨는 {msg}할인{price}원")
print()
calcu("형민",15,4,20000)
calcu("종진",12,5,50000)

x,y=map(int,input("x,y :").split())
def mul(x,y):
    return x*y
print(mul(x,y))

# 함수는 매개변수를 최대한 활용한다.
def qq(a,b):
    for i in range(a,b+1):
        print(i,sep=" ")

qq(1,10)
qq(4,6)

def say(name,old=20,man=True):
    print(name)
    if man:
        print("남")
    else:
        print("여")
say('Tom',False) #매개변수의 갯수가 달라 무엇이 False인지 인식하지 못하기 때문에 man의 초기값인 True가 인식이 된다.
say('july',man=False)

# 효력범위
a = 1 # 전역변수
def vartest(a):
    a = a+1 # 함수 안에서만 이용할 수 있는 지역변수
    print(a)
    return a
vartest(2)
print(a)
a=vartest(3)
print(a)

def plus(x):
    return x+10
print(plus(1))

plus=lambda x:x+10
print(plus(1))

def pp(x):
    return x+20
print(list(map(pp,[1,2,3])))

print(list(map(lambda a: a+20,[1,2,3])))
# map( f , iterable ) : 함수와 반복가능한 자료형을 입력으로 받는다.
# 1. 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수
# 2. map함수의 반환값은 map객체이기 때문에 해당 자료형을 list 또는 tuple형으로 형변환 해줘야한다
# 3. 두번째 인자로 들어오는 반복 가능한 자료형 (list / tuple)을 첫 번째 인자로 들어온 함수에 하나씩 집어넣어 함수를 실행한다

# 1~5까지 list로 표현하는 방법
li=[i for i in range(1,6)]
li2=list(range(1,6))

r=[]
for i in li2:
    r.append(i+1)
print(r)

def one(i):
    return i
r2=list(map(one,li2))
print(r2)

print(list(map(lambda a:a,li2)))

# divmod 몫과 나머지를 튜플형태로 리턴
print(divmod(10,3))

for i,j in enumerate(['python','c','java']):
    print(i,j)

# eval 문자열을 계산해주는 함수
print(eval("1+2"))
print(eval("1*2*3"))
print(eval("'sol'+'desk'"))
print(eval("divmod(10,3)"))


def po(n):
    re=[]
    for i in n:
        if i < 0 :
            re.append(i)
    return re;

n=[3,4,2,-2,10,-3]
print(po(n))

def po(n):
    return n<0

list1=list(filter(po,n))
print(list1)
print(list(filter(lambda a:a<0,n)))

print(max(n))
print(min(n))
print(max("apple")) # 나중에 나오는 문자가 큰 값
print(min("apple")) # 먼저 나오는 문자가 작은 값

print(pow(2,3))
print(2**3)

print(round(4.8))
print(round(4.6891111,2))

print(sorted(n))
print(str("hello".upper()))
print(str(10)) # 정수 10을 문자열로 형 변환해서 출력

print(sum(n))
print(sum(list(range(1,11,2))))
print(sum(tuple(range(1,11))))

print(type("123"))
print(type(n))
print(type([]))
print(type("건용"))
print("아뉜뎁,,, 건용이는 귀여운 타입인뒙,,,,,,,,,,,,,,")

print(type("강사님"))
print("아닌데 강사님은 귀염뽀짝 타입인뎅...")
'''

















