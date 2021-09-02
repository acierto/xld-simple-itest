def assert_true(condition, message=None):
    assert_equals(True, condition, message)

def assert_equals(expected, actual, message=None):
    msg = "Expected "
    if message is not None:
        msg = message + ": " + msg
    if expected != actual:
        raise AssertionError(msg + str(expected) + " but was " + str(actual))
