import pytest

def add(a,b): 
    return a+b


@pytest.mark.parametrize("a, b, expected",[(1,1,2),(2,3,5),(-1,2,1)]) #"a, b, expected" - 함수에 들어갈 인자 

# 함수 하나에 테스트 3개임.
# 테스트할 case를 위와 같이 인자에 쭉 넣으면 됨.
def test_add(a,b,expected):
    assert add(a,b) == expected 