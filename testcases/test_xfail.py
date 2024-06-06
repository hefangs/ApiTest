import pytest


# 正常预期失败，xfailed
@pytest.mark.xfail(reason="0不能做被除数")
def test_one():
    1 / 0
    assert 1 == 1


# 预期意外通过，xpassed
@pytest.mark.xfail(reason="0不能做被除数")
def test_two():
    # 1/0
    assert 2 == 2


if __name__ == '__main__':
    pytest.main()
