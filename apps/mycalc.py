
def add(a,b):
    if not isinstance(a,(int, float))or not isinstance(b,(int,float)):
        raise TypeError("숫자만 입력하세요.")
    return a+b 

def sub(c,d):
    if not isinstance(c,(int, float))or not isinstance(d,(int,float)):
        raise TypeError("숫자만 입력하세요.")
    return c-d 

def div(a,b):
    if not isinstance(a,(int, float))or not isinstance(b,(int,float)):
        raise TypeError("숫자만 입력하세요.") #숫자가 아니면 타입에러
    if b == 0: 
        raise ZeroDivisionError("0으로 나눌 수 없습니다.") #0일 경우 ZeroDivisionError 발생
    return a/b