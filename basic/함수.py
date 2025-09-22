rect_area = 1

def odd_even(x):
    #홀짝 판별 가능
    result = ""
    if x % 2 == 0:
        result = "짝수"
    else:
        result = "홀수"
    return result

# area, length = rect_area(10,20)
# print(f"사각형의 넓이는 {area}, 둘레의 길이는{length} 입니다.")
# area, length = rect_area(20,20)
# print(f"사각형의 넓이는 {area}, 둘레의 길이는{length} 입니다.")

# print(odd_even(3))

def like_fruit(name, fruit="바나나"):
    print(f"{name}님은 {fruit}를 좋아합니다." )


def avg(*nums):
    total = 0 #total 이라고 하는 공간을 만듬
    cnt = len(nums)
    for i in nums:   #(1,2,3)
        total += i #total = total + i
    return total / cnt
print( avg(1,5,6) )
print( avg(1,5,6,2,5) )
print( avg(1,5,6,7,8,9,11) )

like_fruit("홍길동", '사과')
like_fruit("이순신")
like_fruit(fruit="orange", name="이산")

area, length = rect_area(10,20)
print(f"사각형의 넓이는 {area}, 둘레의 길이는{length} 입니다.")
area, length = rect_area(20,20)
print(f"사각형의 넓이는 {area}, 둘레의 길이는{length} 입니다.")

print(odd_even(3))

#def avg