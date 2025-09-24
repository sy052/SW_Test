#test_mycalc_assertion.py

import pytest
import warnings
#import apps.mycalc
from apps.mycalc import add, sub, div

def test_various_asserion():
    #참거짓 검증
    assert True 
    assert 0 == False
    assert 1 == True
    assert not ""
    assert not []

    #비교 검증
    assert 3 + 4 == 7
    assert 5 > 3
    assert 7 != 8

    #멤버 연산자
    assert 'a' in 'apple'
    assert 5 not in[1,2,3]

    #동일성 검증
    a = [1,2]
    b = [1,2]
    c = a
    assert a == b #True
    assert a is not b     
    assert a is c

def test_div_float():
    result = div(1,3)
    assert result == pytest.approx(1/3) #div같은 경우 pytest.approx 활용하기.
    assert div(10,2) == pytest.approx(5.0)

def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(3,0) 

def test_wrong_type():
    with pytest.raises(TypeError):
        add(3, "4")
class DeprecationWarning:
    @staticmethod
    def function_that_warns():
        warnings.warn("This function will be deleted.", DeprecationWarning)
        return True

    # tests/test_mycalc_assertion.py::test_warning FAILED [ 91%]
    def test_warning(): #warning message 확인 테스트
        with pytest.warns(DeprecationWarning, match="제거될 예정"):
            DeprecationWarning.function_that_warns()
            ##result = function_that_warns()
            #assert function_that_warns()