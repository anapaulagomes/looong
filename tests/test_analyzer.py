from looong.analyzer import Analyzer
from looong.method import Method


def test_return_true_when_method_is_detected_with_long_parameter_list():
    method = Method('foo', 'my_python_test_file.py', ['self', 'bar', 'other_bar', 'other_bar_barz'])
    analyzer = Analyzer([])

    assert True is analyzer.has_long_parameter_list(method)


def test_return_false_when_method_is_detected_with_long_parameter_list():
    method = Method('foo', 'my_python_test_file.py', ['self', 'bar'])
    analyzer = Analyzer([])

    assert False is analyzer.has_long_parameter_list(method)
