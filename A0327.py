# """
# 171p 파일 읽고 쓰기
# 
# 파일 객체 = open("새파일.txt", '파일 열기 모드')
#                                 r - 읽기 모드 : 파일을 읽기만 할 때 사용
#                                 w - 쓰기 모드 : 파일에 내용을 쓸 때 사용
#                                 a - 추가 모드 : 파일의 마지막에 새로운 내용을 추가할 때 사용
# 
# ## readline 함수 - 파일의 첫 줄만 인식 가능
# : while문을 통해서 파일을 읽는 작업을 반복
# 
# f = open("C:/doit/새파일.txt", 'r')
# while True:
#     line = f.readline()
#     if not line: break
#     print(line)
# f.close()
# 
# 
# ## readlines 함수 - 파일의 모든 줄을 인식 가능
# : 모든 줄을 저장 가능하기에 반복문이 필요 x
# 
# f = open("C:/doit/새파일.txt", 'r')
# lines = f.readlines()
# for line in lines:
#     print(line)
# f.close
# 
# ## append
# 
# with문과 사용하기 - 176p
# 
# """
# # # with 문 예시
# #
# # # hello.txt 파일 생성 하기
# # with open("hello.txt", 'w') as f:
# #     f.write("hi")
# #
# # # read로 파일 읽어오기 - hi와 같이 문자열 형태로 읽어온다.
# # with open("hello.txt", 'r') as f:
# #     s = f.read()
# #     print(s)
# #
# # # h.txt 파일 생성 하기
# # with open("h.txt", 'w') as f:
# #     for i in range(10):
# #         f.write("{0}".format(i))
# #
# # # readlines로 파일 읽어 오기 - ['0123456789']처럼 리스트 형식으로 출력된다,
# # with open("h.txt", 'r') as f:
# #     l = f.readlines()
# #     print(l)
# #
# # with open("h.txt", 'r') as f:
# #     l = f.read()
# #     print(l)
# 
# """
#  교재 157번 함수
#   - 여러 개의 입력값을 받는 함수 만들기
# """
# 
# 
# # def avg(*args):
# #     sum = 0
# #     for i in args:
# #         sum += i
# #     print(sum / len(args))
# #
# #
# # avg(1, 2)
# # avg(1, 2, 3, 4, 5)
# #
# #
# # # 재귀함수
# #
# # def fac(n):
# #     if n == 1:
# #         return 1
# #     return n * fac(n - 1)
# #
# #
# # print(fac(5))
# 
# 
# # def 함수이름(*매개변수)
# #     수행할 문장
# #     ...
# #
# # 여러개의 수를 입력받기 위해서는 매개변수 앞에 *를 붙여주어야 한다.
# 
# # () 개의 수를 입력 받아, 그 중애서 가장 큰 수를 출력하는 프로그램을 작성하라.
# # def largest(*args):
# #     if len(args) == 0:
# #         return 0
# #     else:
# #         return max(args)
# 
# # max 함수
# 
# # numbers = []
# # for i in range(10):
# #     num = int(input("숫자를 입력하세요: "))
# #     numbers.append(num)
# #
# # max_num = max(numbers)
# # print("입력된 숫자 중 가장 큰 수는", max_num, "입니다.")
# 
# # 람다 표현, 람다 호출
# def plus(x):
#     return x + 10
# 
# 
# print(plus(1))  # 11
# 
# plus = lambda x: x + 10
# print(plus(1))  # 11
# 
# # 람다 표현식 자체로 바로 호출하기!
# plus = (lambda x: x + 10)(1)
# print(plus)  # 11
# 
# 
# def pp(x):
#     return x + 10
# 
# 
# print(list(map(pp, [1, 2, 3])))
# 
# # lamda로 바꿔서 출력
# print(list(map(lambda x: x + 10, [1, 2, 3])))
# 
# # lamda 식에서는 elif 사용 불가능
# a = list(range(1, 11))
# print(list(map(lambda x: str(x) if x % 2 == 0 else x, a)))
# 
# c = [15, 18, 32, 13, 23]
# # 15보다 크고 20보다 작은 값만 걸러서 출력
# print(list(filter(lambda x: x > 15 and x < 20, c)))
# '''
# # 183p ~
# """
# class 클래스이름:
#     def __init__(self): <<< 클래스 자신에 대한 객체 ( 생성자 역할 )
#         self.resilt = 0
#     def add(self, num):
#         self.result += num
#         return self.result
# cal1 = 클래스이름()
# cal2 = 클래스이름()
# 
# 200p __init__ 메서드
# : setdata와 이름만 다르고 모든게 동일하다.
# __init__이므로
# 생성자로 인식되어 객체가 생성되는 시점에 자동으로 호출된는 차이가 있다.
# 
# 
# class Stu :
#     def __init__(self,name,age,adr):
#         self.hello='hi'
#         self.name=name
#         self.age=age
#         self.adr=adr
# 
#     def hi(self):
#         print(f"{self.hello} 나는{self.name}이다")
# 
# a=Stu('건용',28,'서울')
# a.hi()
# print(a.name)
# print(a.age)
# print(a.adr)
# 
# class Person :
#     def __init__(self,*args):
#         self.name=args[0]
#         self.age=args[1]
#     def hi(self) :
#         print("{0}".format(self.name))
# 
# m=Person(*['한희'],20)
# m.hi()
# 
# class Calcu:
#     def __init__(self,*args):
#         self.a=args[0]
#         self.b=args[1]
# 
#     def sum(self):
#         print(self.a+self.b)
#     def minus(self):
#         print(self.a-self.b)
# 
# a=Calcu(3,4)
# a.sum()#7
# a.minus() #-1
# 
# class B:
#     def __init__(self):
#         self.li=[]
# 
#     def bag(self,a):
#         self.li.append(a)
# 
# p=B()
# p.bag('책')
# p.bag('립밤')
# print(p.li)
# a=B()
# a.bag('노트북')
# print(a.li)
# 
# class A :
#     @staticmethod # 정적메소드 : 매개변수에 self를 지정하지 않는다.
#     def add(a,b):
#         print(a+b)
# 
#     @staticmethod
#     def minus(a,b):
#         print(a-b)
# 
# # 정적 메소드이기 때문에 객체 생성없이 클래스로부터 함수에 바로 접근함
# A.add(4,5)
# A.minus(5,4)
# 
# class Stu:
#     def __init__(self,name,age,adr):
#         self.hello='hi'
#         self.name=name
#         self.age=age
#         # 변수앞에 __를 붙여 비공개 속성으로 만들어짐 ( private 와 유사 )
#         # 클래스 안ㅇ서만 사용할 수 있는 비공개 속성 : __속성
#         self.__adr=adr
# 
#     def pr(self,n):
#         # 비공개 속성은 클래스 안에 있는 메소드에서만 접근 가능함
#         self.__adr+=n
#         print(self.__adr)
# 
# a=Stu('형민',20,3000)
# print(a.name)
# # a.__addr+=3000 #클래스 밖에서 비공개 속성에 접근하면 에러발생
# a.pr(3000)
# 
# class Person:
#     #비공개 메소드 : def __함수명
#     def __hi(self):
#         print("안녕")
# 
#     def hello(self):
#         #class 안에서 비공개 메소드 호출 가능
#         self.__hi()
# 
#     #비공개 메소드명이 __hi() 여도 그냥 메소드명을 hi()로 생성이 가능하다
#     def hi(self):
#         print('이것은 hi 메소드')
# 
# 
# 
# c=Person()
# c.hello()
# c.hi()
# # c.__hi()  #class 밖에서 비공개 메소드 호출 불가능
# 
# import random
# like=['건용','초콜릿','아메리카노','국밥','아이스크림']
# a=random.randint(0,len(like)-1) # 인덱스번호로 a를 지정하기위해 len-1
# print(like[a])
# 
# class Student:
#     def __init__(self,id,name,score=0):
#         self.id=id
#         self.name=name
#         self.score=score
#
#     def getID(self):
#         return self.id
#
#     def getName(self):
#         return self.name
#
#     def getScore(self):
#         return self.score
#
#     def setScore(self,score):
#         self.score=score
#
# class Cal:
#     def __init__(self):
#         self.stu=[]
#
#     def add(self,student):
#         self.stu.append(student)
#
#     def avg(self):
#         sum=0
#         for i in self.stu:
#             sum+=i.getScore()
#         average=sum/len(self.stu)
#         return average
#
#
#
# student1=Student(1,'종진')
# student1.setScore(88)
# student2=Student(2,'건용',score=100)
# student3=Student(3,'하니',90)
# student4=Student(4,'형민',99)
#
# calc=Cal()
# calc.add(student1) # 1,'종진',88
# calc.add(student2)
# calc.add(student3)
# calc.add(student4)
#
# print(f"평균 :{calc.avg()}")
# 
# num = list(range(50, 71))
# # 짝수 filter,lambda
# a = list(filter(lambda x: (x % 2 == 0), num))
# print(a)
# # 곱하기 2한값 map,lambda 50*2 51*2 52*2 ...70*2
# b = list(map(lambda x: (x * 2), num))
# print(b)
# 
# 
# class Person:
#     def hi(self):
#         print('안녕하세요')
# 
#     def __init__(self):
#         print("__init__호출")
# 
# class Student(Person):
#     def study(self):
#         print("공부하세요")
#         super().__init__() # 부모클래스를 호출할때 super()
# 
# a=Person()
# a.hi()
# # a.study() # 부모클래스로부터 자식클래스의 함수접근 불가
# b=Student()
# b.hi() # 자식클래스로부터 부모클래스의 함수접근 가능
# b.study()
# 

# 오버라이드 개념
# class Super:
#     def a(self):
#         print("super")
#
# class Sub:
#     def a(self):
#         super().a()
#         print("sub")
# a=Sub()
# a.a()
#
# # 파이썬의 다중상속
# # 자바는 다중상속이 불가능 => 인터페이스 사용
# class Sub2(Super,Sub):
#     def c(self):
#         print("sub2")
#
# s=Sub2()
# s.a()
# s.b()
# s.c()
# 여기부터 오후수업
# a=[1,2,3]
# b=[4,5,6]
# print(a+b)
# a.extend(b) #나열 함수
# print(a)
# 과일={"바나나":4000,"딸기":6000,"망고":4000}
# # 1번 방법
# for 과일이름 in 과일.keys():
#     가격=과일[과일이름]
#     print("{0}는 {1}원 입니다".format(과일이름,가격))
# # 2번 방법
# for 과일이름,가격 in 과일.items():
#     print(f"{과일이름}는 {가격}원 입니다.")
#
# s="This is a note"
# print(s.split())
# # ['This', 'is', 'a', 'note']
#
# a=s.split(" ",maxsplit=1)  #공백 기준으로 1번만 나눈다?
# print(a)
# # ['This', 'is a note']
#
# s="2023/03/27"
# a=s.split("/")
# print(a)
# s="-".join(a) # "-".join(s.split("/")
# print(s)
#
# # iterator 이터레이터
# num=list(range(1,4))
# i=iter(num)
# print(next(i),end=" ")
# print(next(i),end=" ")
# print(next(i))
#
# it=iter(range(1,3))
# print(next(it))
# print(next(it))

# class A :
#     # __init__ : 초기화 생성자 함수??
#     def __init__(self,n):
#         self.n=n
#         self.num=0
#
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.num < self.n:
#             r=self.num
#             self.num+=1
#             return r
#         else:
#             raise StopIteration # 더이상 리턴할 값이 없다면 예외 발생하는 코드?
# for i in A(3):
#     print(i,id(i))
# # 새로운 객체를 생성

# # 제너레이터 : 이터레이터를 생성해주는 함수
# # 반복가능한 객체로 만들어주는 함수
# def n():
#     yield 0
#     yield 1
#
# for i in n():
#     print(i)
#
# # 50이하의 홀수를 반환하는 이터레이터 만들기
# def odd():
#     i=1
#     while i<=50:
#         yield i
#         i+=2
#
# it=odd()
# for i in it:
#     print(i,end=" ,")

# def gen(x):
#     for i in x:
#         yield i
#
# fruit=['apple','banana','mango']
# for i in gen(fruit):
#     print(i,end=",")
#

##################################################
# 모듈
# mod1.py A0327mo
def add(a, b):
    return a + b

def sub(a, b):
    return a-b

######################################################
#   __name__ : 내부적으로 사용하는 특별한 변수
if __name__=="__main__":
    print(add(3,4))
    print(sub(3,1))
    # __name__ 의 이름이 __main__일때 print(add(3,4)),print(sub(3,1))
    # 되므로 다른 파일에서 import로 현재 파일을 받아왔을때 실행되어 지지 않는다.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
