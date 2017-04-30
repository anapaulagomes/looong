from looong.analyzer import Analyzer
from looong.method import Method


def test_should_return_the_method_with_more_parameters():
    method_list = [ Method('foo', 'my_python_test_file.py', ['bar', 'other_bar']),
                    Method('fooo', 'my_python_test_file.py', ['bar']),
                    Method('foooo', 'my_python_test_file.py', ['bar', 'other_bar', 'bar_plus_bar']),
                    Method('fooooo', 'my_python_test_file.py', ['bar', 'other_bar'])]
    analyzer = Analyzer(method_list)
    method_with_more_parameters = analyzer.top_parameter_list()

    assert 'foooo' == method_with_more_parameters.name
    assert 3 == len(method_with_more_parameters.parameters_list)
