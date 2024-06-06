import pytest


# 单参数，单次循环
@pytest.mark.parametrize("name", ["fisher"])
def test_parametrize(name):
    print("我是" + name)


# 单参数，多次循环
@pytest.mark.parametrize("name", ["fisher", "james", "jack"])
def test_parametrize(name):
    print("我是" + name)
