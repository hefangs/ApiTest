import pytest


def test_one():
    assert 1 == 1


@pytest.mark.run(order=2)
def test_two():
    assert 2 == 2


@pytest.mark.run(order=1)
def test_three():
    assert 3 == 4


if __name__ == '__main__':
    pytest.main()
