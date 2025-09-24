# TESTS/test_fixture_scope.py

import pytest

@pytest.fixture(scope="class")

def sample_data():
    print("\n데이터생성")
    return {"id":1, "name":"henry"}

class TestSample: #변수 표기법으로 test를 할 경우 이름을 앞에 test 붙이기
    def test_id(self, calculator_instance): #class는  항상 self. 자기 인자 넣어주기
        #assert sample_data["id"] == 1
        assert calculator_instance.add(3,4) == 7

    def test_name(self, sample_data):
        assert sample_data["name"] == "henry"


class TestGuest:
    def test_empty(self, sample_data): #class는  항상 self. 자기 인자 넣어주기
        assert sample_data["id"] == 1


def test_id(sample_data): 
    assert sample_data["id"] == 1
    
def test_name(sample_data):
    assert sample_data["id"] == 1