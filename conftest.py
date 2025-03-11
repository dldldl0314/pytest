from test_fail_cus import Foo

def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, Foo) and isinstance(right, Foo) and op == "==":
        return [
            "比较两个Foo实例：",
            "值：{} != {}".format(left.val, right.val),
        ]
