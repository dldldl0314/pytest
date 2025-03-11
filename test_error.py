import pytest


def f():
    raise SystemExit(1)


def test_SystemExit():
    # 当调用f()时出现SystemExit异常,则表示程序是正确的.出现其他异常表示程序是错误的
    with pytest.raises(SystemExit):
        f()


def myfunc():
    raise ValueError("返回40013支付错误")


def test_match():
    with pytest.raises((ValueError, RuntimeError), match=r'.*40013.*'):
        myfunc()


if __name__ == "__main__":
    pytest.main(['-s', 'test_error.py'])
