# def sum():
#     num=int(input("num:"))
#     sum=0
#     for i in range(1,num+1):
#         sum=sum+i
#     return sum
#
#   #1+2+3+...+10 -> ()
#   #1+2+3+...+100 -> ()
#
# def sum2():
#     a=int(input("number : "))
#     return a*(a+1)//2
'''
프로그래밍에서 시간 복잡도에 가장 영향을 미치는 것 : 반복문

1~n 까지 합 구하기 -> O(n)
n(n+1)/2 -> O(1) n 과 관계 없이 곱셉,나눗셈,덧셈만 하면 된다

'''
import math

#############################################

# # p.32
# # Q.1-1
# def a(n):
#      sumNum=0
#      for i in range(1,n+1):
#          sumNum+=i*i
#      return sumNum

# # p.39
# # Q.2-1
# def minNum():
#     n = int(input("숫자 입력 :"))
#     li = []
#     liMax=0
#     for i in range(n):
#         n2 = int(input("list에 들어갈 숫자 입력 :"))
#         li.append(n2)
#     for i in range(len(li)):
#         if liMax<=li[i]:
#            liMax=li[i]
#     return liMax
#
# print(minNum())
#
# # 집합
# s = set()
#
# s.add(1)
# s.add(2)
# s.add(2)    # 이미 2가 집합에 있으므로 중복해서 들어가지 않습니다.
#
# print(s)
#
# print(len(s))
#
# print({1,2}=={2,1})

# nameLi=['Tom','Jerry','Mike','Tom']
# def sameName():
#     nameLi=list(input("이름 입력:").split())
#     sameSet=set()
#     for i in range(len(nameLi)):
#         for j in range (i+1,i):
#             if nameLi[i]==nameLi[j]:
#                 sameSet.add(nameLi[j])
#     return sameSet

 # #Q.3-1
 # def aa(a):
 #     n=len(a)
 #     c=set()
 #     for i in range(a-1):
 #         for j in range(i+1,n):
 #             if a[i]!=a[j]:
 #                 c.add((a[i]+a[j]))
 #     return c
 #
 # b=["tom","jerry","mike"]
 # print(aa(b))
#
# 어떤 자연수 p와 q가 있을 때, 만일 p를 q로 나누었을 때 나머지가 0이면 q는 p의 약수이다.
# 6을 예로 들면
# 6 ÷ 1 = 6 … 0
# 6 ÷ 2 = 3 … 0
# 6 ÷ 3 = 2 … 0
# 6 ÷ 4 = 1 … 2
# 6 ÷ 5 = 1 … 1
# 6 ÷ 6 = 1 … 0
# 그래서 6의 약수는 1, 2, 3, 6, 총 네 개이다.
# 두 개의 자연수 a과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을
# 작성하시오.
#
# 출력설명
# 첫째 줄에 a의 약수들 중 K번째로 작은 수를 출력한다. 만일 a의 약수의 개수가 K개보다 적어서
# K번째 약수가 존재하지 않을 경우에는 -1을 출력하시오.

# def K():
#     a=int(input("정수입력 :"))
#     k=int(input("몇 번째 :"))
#     pli=[]
#     for i in range(1,a+1):
#         if a%i==0 and k<a :
#             pli.append(i)
#             pli.sort()
#         elif a%i==0 & k>len(pli) :
#             print(-1)
#     return pli.pop(k-1)
#
# print(K())

'''
N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열중에서 s번째부터 e번째 까지의 수를
오름 차순 정렬했을 때 k번째로 나타나는 숫자를 출력하는 프로그램을 작성하세요.

입력설명
첫 번째 줄에 테스트 케이스 T(1<=T<=10)이 주어집니다.
각 케이스별
첫 번째 줄은 자연수 N(5<=N<=500), s, e, k가 차례로 주어진다.
두 번째 줄에 N개의 숫자가 차례로 주어진다.

출력설명
각 케이스별 k번째 수를 아래 출력예제와 같이 출력하세요.
입력
2
6 2 5 3
5 2 7 3 8 9
15 3 10 3
4 15 8 16 6 6 17 3 10 11 18 7 14 7 15
출력
#1 7
#2 6
입력 해설 :
case 1 : 2 7 3 8의 숫자 중 오름차순 정렬 했을 때 3번째 숫자는 7이다.
case 2 : 8 16 6 6 17 3 10 11의 숫자 중 오름차순 정렬 했을 때 3번째 숫자는 6이다.
'''

# T=int(input())
# for i in range(T):
#     n,s,e,k = map(int,input("n,s,e,k 입력 :").split())
#     a=list(map(int,input("list 입력 :").split()))
#     a=a[s-1:e]
#     a.sort()
#     print(i+1,a[k-1])

# # p.59(문제 - p.38 )
# # Q.4-1 문제 1의 1부터 n까지의 합 구하기를 재귀 호출로 만들어 보세요.
#
# # Q.4-2 문제 2의 숫자 n개 중에서 최댓값 찾기를 재귀 호출로 만들어 보세요.
# v=[17,92,18,33,58,7,33,42]
# def find(n,a):
#     if n==1:
#         return a[0]
#     m = find(n-1,a) # find(7,[])
#
#     if m > a[n-1]:  # m > a[7]
#         return m
#     else:
#         return a[n-1]
#
#
# print(find(len(v),v))   #(8,[17,92,18,33,58,7,33,42])

# # 최대공약수 구하기
#
# # 입력: a, b
#
# # 출력: a와 b의 최대공약수
#
#
# def gcd(a, b):
#     if b == 0:  # 종료 조건
#
#         return a
#
#     return gcd(b, a % b)  # 좀 더 작은 값으로 자기 자신을 호출
#
#
# print(gcd(1, 5))  # 1
#
# print(gcd(3, 6))  # 3
#
# print(gcd(60, 24))  # 12
#
# print(gcd(81, 27))  # 27

# # 피보나치 수열
#
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
# print(fibonacci(10))


# # 리스트에서 특정 숫자의 위치 찾기
#
# # 입력: 리스트 a, 찾는 값 x
#
# # 출력: 찾으면 그 값의 위치, 찾지 못하면 -1
#
#
# def search_list(a, x):
#     n = len(a)  # 입력 크기 n
#
#     for i in range(0, n):  # 리스트 a의 모든 값을 차례로
#
#         if x == a[i]:  # x 값과 비교하여
#
#             return i  # 같으면 위치를 돌려줍니다.
#
#     return -1  # 끝까지 비교해도 없으면 -1을 돌려줍니다.
#
#
# v = [17, 92, 18, 33, 58, 7, 33, 42, 18]
#
# print(search_list(v, 18))  # 2(순서상 세 번째지만, 위치 번호는 2)
#
# print(search_list(v, 33))  # 3(33은 리스트에 두 번 나오지만 처음 나온 위치만 출력)
#
# print(search_list(v, 900))  # -1(900은 리스트에 없음)
#
# # p.83
# # Q.7-1
#
# def allSearch(a,x): #a:list x:찾을 값
#     index=[]
#     for i in range(len(a)):
#         if x==a[i]:
#             index.append(i)
#     return index
#
# print(allSearch(v,18))
#
# # Q.7-2
# # Q.7-3
# stu_no = [39, 14, 67, 105]
# stu_name = ["Justin", "John", "Mike", "Summer"]
#

########################################################
# 선택 정렬이란? ( selection sort )
'''
-주어진 데이터 중 최소값을 찾음
-해당 최소값을 데이터 맨 앞에 위치한 값과 교환

=>처리 되지 않은 데이터 중에서 
가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복한다
ex) data = [8,3,2,1]
    1차 : 1,3,2,8
    2차 : 1,2,3,8
'''
'''
# 쉽게 설명한 선택 정렬

# 입력: 리스트 a

# 출력: 정렬된 새 리스트

# 주어진 리스트에서 최솟값의 위치를 돌려주는 함수

 

def find_min_idx(a):

    n = len(a)

    min_idx = 0

    for i in range(1, n):

        if a[i] < a[min_idx]:

            min_idx = i

    return min_idx

 

def sel_sort(a):

    result = []  # 새 리스트를 만들어 정렬된 값을 저장

    while a:     # 주어진 리스트에 값이 남아 있는 동안 계속

        min_idx = find_min_idx(a)  # 리스트에 남아 있는 값 중 최솟값의 위치

        value = a.pop(min_idx)     # 찾은 최솟값을 빼내어 value에 저장

        result.append(value)       # value를 결과 리스트 끝에 추가

    return result

 

d = [2, 4, 5, 1, 3]

print(sel_sort(d))
'''
'''
# 삽입 정렬이란?
-삽입 정렬은 말 그대로 꽂아 넣는 정렬
-삽입 정렬은 두번째 인덱스부터 시작
-해당 인덱스 (key)앞에 있는 데이터(A)부터 비교해서
key 값이 더 작으면 A값을 뒤 인덱스로 복사
-이를 key값이 더 큰 데이터를 만날 때까지 반복,
큰 데이터를 만난 위치 바로 뒤에 key값을 이동시킨다.

ex) data = [8,3,2,5]
         8
         3 8
         2 3 8
         2 3 5 8
'''
'''
N명의 학생의 수학점수가 주어집니다. N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고,
N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세
요.(평균-학생점수 -> 차이)
평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고(-+), 높
은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 합니다(stu_idx).

입력
첫줄에 자연수 N(5<=N<=100)이 주어지고, 두 번째 줄에는 각 학생의 수학점수인 N개의 자연
수가 주어집니다. 학생의 번호는 앞에서부터 1로 시작해서 N까지이다.
출력
첫줄에 평균과 평균에 가장 가까운 학생의 번호를 출력한다.
평균은 소수 첫째 자리에서 반올림합니다.

입력예제
10
45 73 66 87 92 67 75 79 75 80
출력
74 7
'''
def stu():
    N=int(input("5이상 100이하의 수 입력 : "))
    stu_sc=list(map(int,input("점수 입력 :").split()))
    avg=math.trunc((sum(stu_sc)/N)+0.5)
    scr= {}
    sc=[]
    idx=0
    m=0
    for i in range(N):
        scr[i]=abs(avg-stu_sc[i])
        # enumerate 이용 할 수 있음
        sc=scr.values()
    for i in range(1,len(sc)+1):
        if sc[i-1]<sc[i]:
            m=i




    print(avg)
    print(sc)
    print(scr)

stu()
# #현오씨 코드
# N = int(input())
# scores = list(map(int, input().split()))
#
# avg = round(sum(scores) / len(scores))
#
# h = scores[0]
# m = 0
# for i in range(N):
#     if abs(avg - h) >= abs(avg - scores[i]) and h < scores[i]:
#         h = scores[i]
#         m = i
#
# print(f"{avg} {m + 1}")
#
# # 한빈씨 코드
# N = int(input())
# scores = list(map(int, input().split()))
# avg = round(sum(scores) / len(scores))
# gaps = []
#
# for i, score in enumerate(scores):
#     if score >= avg:
#         gaps.append(score - avg)
#     else:
#         gaps.append(avg - score)
#
# res = []
# minGap = min(gaps)
#
# for i, gap in enumerate(gaps):
#     if minGap == gap:
#         res.append(i)
#
# if len(res) == 1:
#     print("{0} {1}".format(avg, res[0]))
# else:
#     for r in res:
#         if int(scores[r]) > avg:
#             print("{0} {1}".format(avg
# , res[0]))
# else:
#     for r in res:
#         if int(scores[r]) > avg:
#             print("{0} {1}".format(avg, r + 1))
#             break
