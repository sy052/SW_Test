try:
    f = open("output.txt", "w")
except Exception as e:
    print("예외가 발생했습니다", e)
else:
    print("파일오픈 성공")
    f.close

def div(a,b):
    if b == 0:
        raise ZeroDivisionError("0으로 나눌 수 없어요")
    #raise 로 에러발생시킴
    return a/b

div(3,0)