import pytest
# from apps.calculator import Calculator

# #픽스쳐(fixture)
# @pytest.fixture
# def calculator_instance(): # calculator_instance() : decoration 함수 
#     c = Calculator() # 반복되는 함수 지정한 후 변환
#     return c

# def test_add() :
#     c = Calculator()
#     assert c.add(3,4) == 7
def test_add(calculator_instance):
    assert calculator_instance.add(3,4) == 7
    assert calculator_instance.add(-2,-4) == -6

# def test_sub():
#     c = Calculator()
#     assert c.sub(10,4) == 6
#     assert c.sub(-5,-5) == 0
def test_sub(calculator_instance):
    assert calculator_instance.sub(10,4) == 6
    assert calculator_instance.sub(-5,-5) == 0

# def test_div():
#     c = Calculator
#     assert c.div(8,4) == 2
#     assert c.div(100,10) == 10
#     assert c.dif(1,3) == pytest.approx(1/3)
#     with pytest.raises(ZeroDivisionError):
#         c.div(3,0)
def test_div(calculator_instance):
    assert calculator_instance.div(8,4) == 2
    assert calculator_instance.div(100,10) == 10
    assert calculator_instance.dif(1,3) == pytest.approx(1/3)
    with pytest.raises(ZeroDivisionError):
        calculator_instance.div(3,0)