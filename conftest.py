import pytest


@pytest.fixture(scope="function")
def func3():
    print("我是前置步骤3~")
    yield
    print("我是后置步骤3~")
