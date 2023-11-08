from support.assertion_errors import AssertionErrors


class Assertions:
    @staticmethod
    def assert_equal(actual, expected):
        assert actual == expected, AssertionErrors.EQUAL.format(expected, actual)

    @staticmethod
    def assert_check(expected, actual):
        assert expected in actual, AssertionErrors.EQUAL.format(expected, actual)