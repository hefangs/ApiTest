import pytest


def setup_module():
    print("准备测试数据")


def teardown_module():
    print("清除测试数据")


def test_one():
    print("one")
    assert 1 == 1


def test_two():
    print("two")
    assert 2 == 2


if __name__ == '__main__':
    pytest.main()
