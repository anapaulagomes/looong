from looong.extractor import Extractor
from looong.method import Method
from looong.codefile import CodeFile
import os
import pytest
import mock
from mock import mock_open


@pytest.fixture()
def os_mock(mocker):
    directory = '/tests/fixtures'
    mocker.patch('os.getcwd', return_value='/home/bla')
    yield mocker.patch('os.walk', return_value=[(directory, [], ['foo.py'])])


def test_should_return_method_with_one_parameter_when_extract_from_method_with_one_parameter(mocker, os_mock):
    extractor = Extractor('/tests/fixtures')

    file_mock = mock.mock_open(read_data='def foo(bar):')
    with mock.patch('builtins.open', file_mock, create=True):
        code_files = extractor.code_files()

    methods = code_files[0].method_list[0].parameters_list

    assert ['bar'] == methods


def test_should_extract_multiple_parameters_on_method_parameter_list(mocker, os_mock):
    extractor = Extractor('/tests/fixtures')

    file_mock = mock.mock_open(read_data='def foo(bar, other_bar):')
    with mock.patch('builtins.open', file_mock, create=True):
        code_files = extractor.code_files()

    methods = code_files[0].method_list

    assert ['bar', 'other_bar'] == methods[0].parameters_list


def test_should_return_a_method_with_an_empty_list_when_there_is_no_parameters_on_method_parameter_list(mocker, os_mock):
    extractor = Extractor('/tests/fixtures')

    file_mock = mock.mock_open(read_data='def foo():')
    with mock.patch('builtins.open', file_mock, create=True):
        code_files = extractor.code_files()

    assert [] == code_files[0].method_list[0].parameters_list


def test_should_return_parameters_list_extracted_from_a_file():
    extractor = Extractor('/tests/fixtures')
    code_files = extractor.code_files()

    assert []                   == code_files[0].method_list[0].parameters_list
    assert ['bar']              == code_files[0].method_list[1].parameters_list
    assert ['bar', 'other_bar'] == code_files[0].method_list[2].parameters_list
    assert ['*bar']             == code_files[0].method_list[3].parameters_list
    assert ['**bar']            == code_files[0].method_list[4].parameters_list


def test_should_return_code_file_with_methods_list():
    extractor = Extractor('/tests/fixtures')
    code_files = extractor.code_files()

    assert 'my_python_test_file.py' == code_files[0].filename
