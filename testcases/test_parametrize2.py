import pytest


# 多参数，多次循环
@pytest.mark.parametrize(["name", "age"], [["fisher", 18], ["james", 26], ["jack", 35]])
def test_parametrize(name, age):
    print(f"{name}的年龄是{age}")
