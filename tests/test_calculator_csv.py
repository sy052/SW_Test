#tests/test_calculator_csv.py

import csv
import pytest

def load_cases(path):
    cases = []
    with open(path, newline="", encoding="utf-8-sig") as f: 
        reader = csv. DictReader(f)
        for row in reader: #한줄한줄씩 읽어옴
            print(row)
            a = row['a']
            b = row['b']
            expected = row['expected_result']
            cases.append((a, b, expected))
    return cases

# ADD_CASES = load_cases("tests/data/add.csv")
# print(ADD_CASES)

def trans(s):
    if s == "":
        return None
    try:
        return int(s)
    except ValueError:
        return s #숫자로 못바꾸면 그대로 문자열로 쓰겠다.
    

ADD_CASES = load_cases("tests/data/add.csv")
print(ADD_CASES)


@pytest.mark.parametrize("a, b, expected", ADD_CASES)
def test_and_from_csv(calculator_instance, a, b, expected):
    #assert calculator_instance(a,b) == expected
    a = trans(a)
    b = trans(b)
    expected = trans(expected) #if expected is not None else  None
    if expected == "TypeError":
         with pytest.raises(TypeError):
             calculator_instance.add(a,b)
    else:
         assert calculator_instance.add(a,b) == expected

    # if expected == "TypeError":
    #     # with pytest.raises(TypeError):
    #     #     calculator_instance.add(a,b)
    #     pass
    # else:
    #     #assert calculator_instance(a,b) == expected
    #     pass


    