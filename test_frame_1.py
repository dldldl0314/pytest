# tset_frame_1.py

import pytest


def setup_module():
    print("\nsetup_module: 整个test_module模块只执行一次")


def teardown_module():
    print("teardown_module: 整个test_module模块只执行一次")


def setup_function():
    print("setup_function: 每个测试函数开始前都会执行")


def teardown_function():
    print("teardown_function: 每个测试函数结束后都会执行")


# 测试模块中的用例1
def test_one():
    print("正在执行测试模块的test1")


# 测试模块中的用例2
def test_two():
    print("正在执行测试模块的test2")


if __name__ == "__main__":
    pytest.main(["-vs", "tset_frame_1.py"])
