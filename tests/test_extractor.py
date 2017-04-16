from looong.extractor import Extractor
from looong.method import Method
from mock import patch


@patch('builtins.open')
def test_should_return_method_with_one_parameter_when_extract_from_method_with_one_parameter(file_mock):
    file_mock.read.return_value = 'def foo(bar):'
    file_mock.name.return_value = 'foo.py'

    extractor = Extractor(file_mock)

    methods = extractor.methods()
    expected_parameters = ['bar']

    assert methods[0].parameters_list == expected_parameters


@patch('builtins.open')
def test_should_extract_multiple_parameters_on_method_parameter_list(file_mock):
    file_mock.read.return_value = 'def foo(bar, other_bar):'
    file_mock.name.return_value = 'foo.py'

    extractor = Extractor(file_mock)

    methods = extractor.methods()
    expected_parameters = ['bar, other_bar']

    assert methods[0].parameters_list == expected_parameters
