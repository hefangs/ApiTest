import pytest


# 用例筛选
# 1 注册，pytest.ini
# 2 使用，@pytest.mark.api
# 3 筛选，pytest -m api

@pytest.mark.api
def test_one():
    assert 1 == 1


@pytest.mark.db
def test_two():
    assert 2 == 2


if __name__ == '__main__':
    pytest.main()
