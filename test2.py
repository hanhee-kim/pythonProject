# # p.322~p.329
# # Q. 1
# str="a:b:c:d"
# sp=str.split(":")
# print("#".join(sp))

# print(str.replace(":","#"))


# # Q. 2
# a = {'A':90,'B':80}
# a['C']=70
# print(a['C'])


# # Q. 3
# a=[1,2,3]
# a=a+[4,5]
# print(a)
#
# a=[1,2,3]
# a.extend([4,5])
# print(a)

# '''
# 같은 표현식이지만
# 첫번째의 코드는 결합연산자(+)를 사용한다.
# 이 경우 a와 [4,5] 두 리스트를 결합하여 새로운 리스트를 만들고
# 이를 다시 a에 할당한다.a리스트 자체는 변경되지 않는다.
# 'a'리스트의 변경을 원하지 않거나,
# 'a' 리스트와 결합할 리스트가 이미 존재하는 경우에
#  새로운 리스트를 만들어서 사용하는 것이 좋다.
#
# 두번째의 코드는 extend메서드를 사용한다.
# 이 경우 a리스트의 끝에 [4,5] 리스트를 추가합니다.
# a 리스트 자체가 변경이 된다.
# '''


# # Q. 4
# A=[20,55,67,82,45,33,90,87,100,25]
# sum=0
# for i in range(len(A)):
#     if A[i]>=50:
#         sum+=A[i]
# print(sum)


# # Q. 5
# def p():
#     num=int(input("정수입력 :"))
#     li=[0,1]
#     i=0
#     while True:
#         a=li[i]+li[i+1]
#         if a<=num:
#             li.append(a)
#         else:
#             break
#         i+=1
#     print(li)
#
# p()


# # Q. 6
# def totalSum():
#     num=list(map(int,input("','를 기준으로 정수를 입력하세요 : ").split(",")))
#     total=sum(num)
#     return total
# print(totalSum())

# # Q. 7
# def gugu():
#     num=int(input("알고 싶은 단 :"))
#     for i in range(1,10):
#         print (num*i,end=" ")
# gugu()

# # Q.8
#
# with open("abc.txt","r")as f :  # abc.txt 를 f 라고 칭함
#     a=f.readlines()  # a 의 type 은 list
#     a.reverse()
#     print(a)
#
# with open("abc.txt","w")as f:
#     for i in a :
#         li=i.strip()    # strip : 문자를 지울때
#         f.write(li)
#         f.write('\n')

# # Q. 9
#
# with open("sample.txt","r")as txt:
#     a=[]
#     read=txt.readlines()
#     for i in read:
#         sample=int(i.strip())
#         a.append(sample)
#     avg=sum(a)/(len(read)+1)
# print(sum(a),round(avg))
#
# with open("result.txt","w")as txt:
#     txt.write("total : "+str(sum(a)))
#     txt.write("\n")
#     txt.write("average : "+str(avg))


# # Q. 10
# class Calculator :
#     def __init__(self,li):
#         self.li=li
#
#     def sum(self):
#         total=sum(self.li)
#         print(total)
#     def avg(self):
#         print (sum(self.li)/(len(self.li)))  #len()길이보단 요소의 수
#
#
# cal1=Calculator([1,2,3,4,5])
# cal1.sum()
# cal1.avg()
# cal2=Calculator([6,7,8,9,10])
# cal2.sum()
# cal2.avg()


# Q. 12
# 답: 7
# try 문에서
# 첫 줄 -> 없는 인덱스 번호를 찾고
# 두번째 줄 -> type이 맞지않고,
# 세번째 줄 -> 0으로 나눌수 없다.
# 첫번째 줄에서 이미 예외가 발생하였으므로, exception IndexError발생
# result의 값은 0+3=3이됨
# 이후 finaly 는 반드시 실행이 되기 때문에 result+4
# 즉 result=3+4=7 이 되며
# print 했을때 7 이 출력된다.

# # Q. 13
# def DashInsert() :
#     number=input("숫자입력")
#     numberList=list(map(int,list(number)))
#     str1=[]
#     for i in range(0,len(numberList)-1):
#         str1.append(numberList[i])
#
#         if numberList[i] % 2 == 1 and numberList[i+1] % 2 == 1:
#             str1.append("-")
#         elif numberList[i]%2 == 0 and numberList[i+1] % 2 ==0 :
#             str1.append("*")
#     str1.append(numberList[-1])
#
#     s=list(map(str,str1))
#     print("".join(s))
#
# DashInsert()

# # Q. 14
# def rep():
#     s=input("문자열 입력 :")
#     n=list(s)
#     N=[]
#     count=1
#     for i in range(1,len(s)) :
#         if n[i-1]==n[i]:
#             count+=1
#         else:
#             N.append(n[i-1])
#             N.append(str(count))
#             count=1
#
#     N.append(n[len(s)-1])
#     N.append(str(count))
#     print("".join(N))
# rep()


# # Q. 15
# def Du():
#     n=list(map(str,input("0~9까지의 숫자 입력 : ").split()))
#     result=""
#     for i in range(len(n)):
#         if len(list(n[i]))!=10:
#             result="false"
#             print(result)
#         else:
#             if len(set(list(n[i]))) != len(list(n[i])):
#                 result="false"
#                 print(result)
#             else:
#                 result="true"
#                 print(result)
# Du()

# # Q. 16
# def mos():
#     dic = {
#      '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
#      '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
#      '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
#      '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
#      '-.--':'Y','--..':'Z'
#     }
#     a=list(input("모스부호 입력 :").split("  "))
#     n=len(a)
#     print(a)
#     pr=[]
#     for i in range(n):
#         b=a[i]
#         c=b.split()
#         for j in range(len(c)):
#            if dic[c[j]] :
#                pr.append(dic[c[j]])
#         pr.append(" ")
#     print("".join(pr))
#
# mos()

import re

# Q. 17
#  2번

# # Q. 18
#
# p = re.compile("[a-z]+")    # a~z까지의 소문자를 반복
# m = p.search("5 python")    # p의 식을 저 문자열에서 검색해 -> python
# c = m.start() + m.end()
# #    p의 index->2
# #    n의 index->7 end = n index+1
# print(m)
# print(m.end())
# print(c)
# 10

# Q. 19
# Q. 20


# # p.179~181
# # Q .1
#
# def if_odd(n):
#     if n % 2 == 1:
#         return True
#     else:
#         return False


# # Q .2
# def avg_numbers(*args):
#     result = 0
#     for i in args:
#         result += i
#         avg = result / len(args)
#     return avg
#
#
# print(avg_numbers(1, 2))
# print(avg_numbers(1, 2, 3, 4, 5))

# # Q. 3
# input1, input2 = map(int, input("숫자 두개를 공백기준으로 작성해주세요").split())
#
# total = input1 + input2
# print("두 수의 합은 %s 입니다." %total)
# print("두 수의 합은 {0} 입니다.".format(total))

# # Q. 4
# # 4
# print("you" "need" "python")
# print("you" + "need" + "python")
# print("you", "need", "python")  # , 기준이면 ? 각 string 단어마다 공백기준으로 나뉘어 나옴
# print("".join(["you" , "need" , "python"]))

# # Q. 5
# with open("test.txt","w")as f1:
#     f1.write("Life is too short")
#
# with open("test.txt","r")as f2:
#     print(f2.readline())
#

# # Q. 6
# user_input=input("저장할 내용을 입력하세요 :")
# f = open("te.txt","a")  #a : 추가 모드
# f.write(user_input)
# f.write("\n")
# f.close()
#

# # Q. 7
# with open("test3.txt","r")as f :
#     body=f.read()
#     f.close()
#     body=body.replace("java","python")
#
# with open("test3.txt","w")as f:
#     f.write(body)
#     f.close()


# p.262~265
# Q. 1
