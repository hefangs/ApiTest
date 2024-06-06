import pytest


# 装饰器
# 共享范围scope默认是function(同一个函数内只执行一次)
# 其他包括class(同一个class内), module(同一个文件内), package(同一个目录内), session(同一次执行内的所有用例)
# autouse默认是False，需要收手动传入指定的方法中
# fixture一般结合conftest使用，统一管理，pytest会自动检测
@pytest.fixture()
def func1():
    print("我是前置步骤1：连接数据库，启动浏览器，生成测试数据")
    yield 6
    print("我是后置步骤1：关闭数据库，关闭浏览器，删除测试数据")


@pytest.fixture(scope="function", autouse=True)
def func2():
    print("我是前置步骤2~")
    yield  # 生成器
    print("我是后置步骤2~")


def test_one(func1):
    assert 1 == 1


def test_two():
    assert 2 == 2


def test_three(func3):
    assert 3 == 3


if __name__ == '__main__':
    pytest.main()
