import pytest


# fixture数据共享
@pytest.fixture(scope="module")
def func1():
    print("我是前置步骤1：连接数据库，启动浏览器，生成测试数据")
    yield
    print("我是后置步骤1：关闭数据库，关闭浏览器，删除测试数据")


def test_one(func1, doctest_namespace):
    doctest_namespace["name"] = "fisher"
    assert 1 == 1


def test_two(func1, doctest_namespace):
    name = doctest_namespace["name"]
    print(f"我是{name}")
    assert 2 == 2


if __name__ == '__main__':
    pytest.main()
