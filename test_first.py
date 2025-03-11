import pytest


def test_1():
    print("this is test1")


if __name__ == "__main__":
    pytest.main(["-s", "test_first.py"])
