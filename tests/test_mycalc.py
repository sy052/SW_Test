import pytest
from apps.mycalc import add, sub
#외부에 있는 파일 import
# import app 

#def add(a,b): 숫자 a,b 여기서 지정.
#print(add(3,4))
#7이라는 구문을 제대로 테스트하는지 알아보기 => assert 조건식
def test_add_positive_num():
    assert add(3,4) == 7
    assert add(31,4) == 35
    #준비
    a = 3
    b = 4
    expected_result = 7
    #실행
    actual_result = add(3,4)

    #검증
    assert actual_result == expected_result

def test_add_negative_num():
    assert add(-2,-4) == -6

def test_sub_positive_num():
    assert sub(2,4) ==-2

def test_sub_negative_num():
    assert sub(-2,-4) == 2