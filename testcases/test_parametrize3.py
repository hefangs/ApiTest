import pytest

from util.read_data import get_data


# 多参数，多次循环
@pytest.mark.parametrize("name,age", get_data()["hero_list"])
def test_parametrize(name, age):
    print(f"{name}的年龄是{age}")
