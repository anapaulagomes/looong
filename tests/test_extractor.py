from looong.extractor import Extractor
from looong.method import Method
from mock import patch
from mock import mock_open


@patch('__main__.open')
def test_should_return_method_with_one_parameter_when_extract_from_method_with_one_parameter(file_mock):
    file_mock.read.return_value = 'def foo(bar):'
    file_mock.name.return_value = 'foo.py'

    extractor = Extractor(file_mock)

    methods = extractor.methods()
    expected_parameters = ['bar']

    assert methods[0].parameters_list == expected_parameters


@patch('__main__.open')
def test_should_extract_multiple_parameters_on_method_parameter_list(file_mock):
    file_mock.read.return_value = 'def foo(bar, other_bar):'
    file_mock.name.return_value = 'foo.py'

    extractor = Extractor(file_mock)

    methods = extractor.methods()
    expected_parameters = ['bar', 'other_bar']

    assert methods[0].parameters_list == expected_parameters


@patch('__main__.open')
def test_should_return_a_method_with_an_empty_list_when_there_is_no_parameters_on_method_parameter_list(file_mock):
    file_mock.read.return_value = 'def foo():'
    file_mock.name.return_value = 'foo.py'

    extractor = Extractor(file_mock)

    methods = extractor.methods()
    expected_parameters = []

    assert methods[0].parameters_list == expected_parameters


def test_should_return_parameters_list_extracted_from_a_file():
    code_file = open('tests/fixtures/my_python_test_file.py')

    extractor = Extractor(code_file)

    methods = extractor.methods()

    expected_file_name = 'my_python_test_file.py'
    expected_methods = [Method('foo', expected_file_name, []),
    Method('fooo', expected_file_name, ['bar']),
    Method('foooo', expected_file_name, ['bar', 'other_bar']),
    Method('fooooo', expected_file_name, ['*bar']),
    Method('foooooo', expected_file_name, ['**bar']),
    ]

    assert methods[0].parameters_list == expected_methods[0].parameters_list
    assert methods[1].parameters_list == expected_methods[1].parameters_list
    assert methods[2].parameters_list == expected_methods[2].parameters_list
    assert methods[3].parameters_list == expected_methods[3].parameters_list
    assert methods[4].parameters_list == expected_methods[4].parameters_list
