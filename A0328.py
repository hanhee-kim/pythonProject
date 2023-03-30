# f=open('나는 없는 파일','r')
# 없는 파일이라 읽어올 수 없기 때문에 오류 ( file not find )
# try :
#   except[발생오류 [as 오류 메세지변수]] :
# try:
#     x=int(input("나눌 숫자 입력"))
#     y=10/x
#     print(y)
# except:
#     print("예외발생")
#
# li=[1,2,3]
# try:
#     x,y=map(int,input("인덱스,나눌 숫자 입력").split())
#     print(li[x]/y)
# except ZeroDivisionError:
#     print("0으로 나눌 수 없다")
# except IndexError:
#     print("잘못된 인덱스")

# raise : 일부러 오류를 발생 시킴
# try:
#     x=int(input("2의 배수 입력"))
#     if x%2!=0:
#         raise Exception("2의 배수가 아니다")
#     print(x)
# except Exception as e:
#     print("예외발생",e)
# # => class로 바꾸는 작업
# class E(Exception):
#     def __init__(self):
#         super().__init__('2의 배수 아님')
#
# def a():
#     try:
#         x=int(input('2의 배수 입력'))
#         if x%2 != 0 :
#             raise E
#         print(x)
#     except Exception as e:
#         print("예외발생",e)
# # a함수 호출시 2의 배수가 아닐때 raise로 예외발생 E ( e에 해당하는 에러메세지 출력)
# a()

# # -datetime-
# import datetime
#
# print(datetime.date.today())
# t=datetime.date(2023,3,28)
# t=t+datetime.timedelta(weeks=1)
# print(t)

# # 오늘을 기준으로 D-day를 출력
# a=datetime.date(2023,12,25)
# a2=datetime.date()
# diff=a-a2
# print("D-day",diff.days,"일")

# import time
# print(time.strftime('%Y/%m/%d/%H/%M'))
#
# a=datetime.datetime.now()
# print(a.strftime('%Y/%m/%d/%H/%M'))


# # 1. 1부터 30까지의 숫자 중 홀수를 각 라인 단위로 파일에 입력하는 프로그램을 작성해라
# # 파일이름은 odd.txt
#
# with open("odd.txt","w")as f:
#     for i in range(1,31):
#         if(i%2==1):
#             f.write("%d\n"%i)
#
# # 2. 리스트가 주어질때, 자신을 제외한 곱셈을 출력해라.
# # 입력 : ex=[1,2,3,4]  출력 : [24,12,8,6]
# a=list(map(int,input("정수 입력 :").split()))
# b=1
# c=[]
# for i in range(len(a)):
#     b=1
#     for j in a :
#         if a[i]==j:
#             continue
#         else:
#             b=b*j
#     c.append(b)
# print(c)

# 3.Calculator class를 작성해라
# class Calculator:
#     def __init__(self,n):
#         self.n=n
#     def sum(self):
#         print(sum(self.n))
#     def avg(self):
#         print(sum(self.n)/(len(self.n)))
#
# cal1=Calculator([1,2,3,4,5]) #+5
# cal1.sum() #15
# cal1.avg() #3.0
# cal2=Calculator([6,7,8,9,10])
# cal2.sum() #40
# cal2.avg() #8.0


# 4.	사용자로부터 리스트 형식 [data1],[data2],[data3]과 같은 형식으로 데이터를 입력받아, 한줄에 하나씩 데이터를 출력해라.
# ex) 입력: [aa],[bb],[cc],[dd]
#     출력: aa, bb, cc, dd
# str=list(map(list,input("입력하세용").split(",")))
# for i in range(len(str)):
#     print(str.__getitem__(i))

# 5. Area class
# class Area:
#     def __init__(self):
#         self.num1=0
#         self.num2=0
#         self.color=""
#     def set(self,num1,num2,color):
#         self.num1 = num1
#         self.num2 = num2
#         self.color = color
#     def get(self):
#         return self.num1*self.num2,self.color
#
# a1=Area()
# a2=Area()
# a1.set(10,6,'red')
# a2.set(4,4,'blue')
# print(a1.get())
# print(a2.get())

##json,pickle
# import json
# d={"a":40,
#    "b":("a",3,4),
#    "c":"python"}
#
# f="test.json"
#
# with open(f,"w")as f:
#     json.dump(d,f) # 저장
#
# with open("test.json","r")as f:
#     data=json.load(f)
#     print(d["a"])
#     print(d["b"])
#     print(d["c"])

# 정규표현식을 지원하는 모듈 re ( regular expression )
import re
# p = re.compile('[a-z]+')
# m=p.match("python")
# print(m)

''' 정규 표현식 '''
# import re
#
# w = ['orange', 'order', 'october', 'march', 'young', 'hanini']
#
# p = r"oc.*" # oc.* : oc로 시작하는 모든 문자, * : 반복
# for i in w:
#     if re.match(p, i):  # p에 해당하는 조건과 일치하는지 여부
#         print(i)

# b 로 시작하고 y 로 끝나는 패턴
# p=b".*y"

print(re.search(r"^abc$","abc"))
print(re.search(r"^abc$","abcd"))
print(re.search(r"^abc$","xabcd"))

w=['soup','spot','book','notebook','sdd']
p=r"^s...$"     # ... : 모든문자(3글자)
a=[i for i in w if re.search(p,i)]
print(a)

print(re.search(r"ba*","b"))
print(re.search(r"ba{1,3}","baaaaaaaaaaaaaaa"))

s="I like pink colour"
p=r"w+ (color|colour)"

print(re.search(p,s))

p=re.compile('(ABC)+')
m=p.search('ABCABCABC OK?')
print(m)
print(m.group())

p=re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
m=p.search("park 010-1234-1234")
print(m)
print(m.group(1))