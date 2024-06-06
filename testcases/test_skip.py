import pytest


def test_one():
    assert 1 == 1


@pytest.mark.skip(reason="用户不执行")
def test_two():
    assert 2 == 2


@pytest.mark.skipif(2 > 3, reason="有条件跳过")
def test_three():
    assert 3 == 3


if __name__ == '__main__':
    pytest.main()
