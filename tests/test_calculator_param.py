#tests/test_calculator_param.py
import pytest

add_test_cases = [ #리스트 안에 튜플 형태로 ..
    (2,3,5),
    (-1,-1,-2),
    (5,-3,2),
    (-5,3,-2),
    (0,1,1),
    (0.1,0.2, pytest.approx(0.3)),
    (10000000, 20000000, 30000000),
    pytest.param(10000000, 20000000, 30000000, id="large numbers")
]

@pytest.mark.parametrize("a, b, expected", add_test_cases) #문자열 형태로 나열해야 함. [변수]리스트 형태로 TC 만듬 
def test_add_cases(calculator_instance, a, b, expected):
    assert calculator_instance.add(a, b) == expected

# 예외테스트 파라미터화
div_test_cases = [ #리스트 안에 튜플 형태로 ..
    #(10, 2, 5),
    (10, 0, ZeroDivisionError),
    ("10", 2, TypeError),
    (10, "2", TypeError),
    # (5,"1",TypeError),
    (None, 3, TypeError)
    # (10,None,TypeError)
]
@pytest.mark.parametrize("a, b, expected", div_test_cases)
def test_div_cases(calculator_instance, a, b, expected):
    with pytest.raises(expected):
        calculator_instance.div(a, b)

@pytest.mark.parametrize("x", [1,2])
@pytest.mark.parametrize("y", [10,100])
def test_multiparam_cases(x, y):
    assert isinstance(x, int)
    assert isinstance(y, int)
