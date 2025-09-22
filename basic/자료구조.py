# 문자열
str1="황깜비"

print(str1[0])
print(str1[1])
print(str1[2])
print(str1[:3])

# 데이터
data = "python is easy language."
print(data.count('p'))
# print(data.find('p'))
print(data.find('x'))
print(data.index('p'))
print(data.replace('python','java'))
print("!!!!")
#<class 'str'>
print(type(data))

data2 = " henry, 010-1234-5678 "
print(data2.strip())
print(data2.split(','))
print(type(data2))
print("!!!")

# 리스트
list1 = list() #리스트 생성자도 클래스임.
print(type(list1))
list2 = []
list3 = ['henry', '25', 'False'] # 생성
list3.append('170.5') # 순차적으로 추가이므로 마지막에 추가됨
print(list3)
list3.insert(2,'69.5') # 중간에 추가
list3[1] = 26 # 두번째의 값을 26으로 바꿔
print(list3)
list3.remove("henry")
print(list3) # [26, '69.5', 'False', '170.5']
list3.pop(0) # index를 제거 => 
print(list3) # ['69.5', 'False', '170.5']
list3.clear()
print(list3)

list4 = ['henry', 25, False, 170.5, 52.7] # 생성
print(list4[0])
print(list4[:3])
print(list4[3:])
print(list4[:2]) # 나이를 뽑으려면 인덱스는 1이 더 커야 하므로 2.

list1 = [1,2,3]
list2 = [4,5,6]
print(list1 + list2)
print(list1 * 3)

# 튜플 : 참조하여 적을 경우는 튜플 형태로.
t = ("henry",25,39.5)
# t[1] = 26
print(t[1])

# packing / unpacking
#name, age, height = t
n, a, w = t
print(n) #t[0]
n, *d = t
print("!!!") 
print(d) 


#dictionary
dict1 = {"name":"henry", "age":25, "weight": 70.5}
print( dict1["name"] )
#dict1["hobby"] = "football"
# 취미를 두개를 적으려면 리스트[]형식으로
dict1["hobby"] = ["football", "sing"]
print( dict1 )
dict1["age"] = 26
print(dict1)
dict1.pop("name")
#dict2 = print(dict1)
print(dict1, "!!!")

#dict1.clear()
print(dict1)
#print(dict1)
#dict1["hobby"] 

#dictionary {키 : 값}
print(dict1.items())
print(dict1.keys())
print(dict1.values())

#################################
# # 유저로부터 점수를 입력받는다.
# # A : 100~81, B:80~61, C:60~0
# score = int(input("점수를 입력해"))
# if score >= 81:
#     print("A")
# elif score >= 61:
#     print("B")
# else:
#     print("C")
# ###
# # 사용자로부터 두 수를 입력받아라.
# # 둘 중에 큰 수를 출력하라.
# print("score2 조건문")
# num1 = int(input("첫번째 숫자"))
# num2 = int(input("두번째 숫자"))
# num3 = int(input("세번째 숫자"))
# score2 = 100 (input("점수를 입력해"))
# if score >= 81:
#     print("A")
# elif score >= 61:
#     print("B")
# else:
#     print("C")

# 사용자로부터 입력받은 숫자가 홀수인지 짝수인지 출력
# 6%2
num = int(input("숫자입력"))
if num %2 == 0 :
    print("짝수")

else:
    print("홀수")


id = "050104-3214555" #string은 하나하나 자리수가 있음
print(id[7]) #'3'
# if id[7] %2 == 0 :
#     print("여자")
# else:
#     print("남자")
#####
if id[7] == '1' or id[7] =='3' :
     print("남자")
else:
    print("여자")
#############################
if int(id[7]) %2 == '0' :
    print("여자")
else:
    print("남자")

############################
file = "hello.py"
print(file.split('.')[1])
if file.split('.')[1] == 'py' :
    print("python 파일")


# for
for i in [1,2,3]:
    print(i) #1,2,3 순서로 출력되고 3을 끝으로 마침.
print("###")
for j in range(1,4,1): #1이상 4미만이며 step=1 이므로 1씩 증가.
    print(j)
print("###")
for x in range(4): #0123
    print(x)
print("###")
for i0 in range(10,-1,-1): #10,9,8,...,0
    print(i0)
print("###")
for i1 in range(1,10,1):
    print(i1)
print("###아래와 같은 식###")
#초기식
i2 = 1
# while 조건식:
#     명령문
#     변화식
while i2<10:
    print(i2)
    i2 = i2 + 1 
print("###")

i3 = 6
while True:
    print(i2)
    i3 = i3 + 1 #i+=1
    if i3>5:
        break 

# 짝수만...
for i4 in range(0, 5, 2):
    print(i4)
print("###i4###")
i5=0
while i5<5:
    print(i5)
    i5 = i5 + 1 
    # i5 = i5 + 2  와  i5 += 2는 같은 뜻
    if i5%2 == 1:
        #print(i5)
        continue #아래 명령문을 수행하지 않을 때 continue 사용함.
print(f"continue {i5}")

for i7 in range(1,11):
    print(f"{i7}마리 코끼리가 거미줄에 걸렸네.") #f스트링

dan = int(input("단을 입력하세요(2~9)"))
for i8 in range(1, 10):
    print(f"{dan} x {i8} = {dan*i8}")

# while문을 사용하라.
# 사용자한테 비번을 입력받아라.
#  비번이 같으면 "성공" 출력하고 종료
# 다르면 "실패" 출력하고, 다시 입력
# 비밀번호 = "1234"
pw = 1234
input_pw = int(input())
while input_pw == 1234:
    print(f"성공")
    i5 = i5 + 1 
    # i5 = i5 + 2  와  i5 += 2는 같은 뜻
    if i5%2 == 1:
        #print(i5)
        continue #아래 명령문을 수행하지 않을 때 continue 사용함.
print(f"continue {i5}")
####################
while True:
    pw = input("비밀번호입력")
    if pw == "1234" :
        print("성공")
        break
    else:
        print("실패")
