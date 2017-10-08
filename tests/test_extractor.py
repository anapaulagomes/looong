import os
import mock


def test_should_return_method_with_one_parameter_when_extract_from_method_with_one_parameter(
        os_mock, extractor):
    file_mock = mock.mock_open(read_data='def foo(bar):')
    with mock.patch('builtins.open', file_mock, create=True):
        methods_list = extractor.all_methods()

    methods = methods_list[0].parameters_list

    assert methods == ['bar']


def test_should_extract_multiple_parameters_on_method_parameter_list(
        os_mock, extractor):
    file_mock = mock.mock_open(read_data='def foo(bar, other_bar):')
    with mock.patch('builtins.open', file_mock, create=True):
        methods_list = extractor.all_methods()

    assert methods_list[0].parameters_list == ['bar', 'other_bar']


def test_should_return_a_method_with_an_empty_list_when_there_is_no_parameters_on_method_parameter_list(
        os_mock, extractor):
    file_mock = mock.mock_open(read_data='def foo():')
    with mock.patch('builtins.open', file_mock, create=True):
        methods_list = extractor.all_methods()

    assert methods_list[0].parameters_list == []


def test_should_return_parameters_list_extracted_from_a_file(extractor):
    methods_list = extractor.all_methods()

    assert methods_list[0].parameters_list == []
    assert methods_list[1].parameters_list == ['bar']
    assert methods_list[2].parameters_list == ['bar', 'other_bar']
    assert methods_list[3].parameters_list == ['*bar']
    assert methods_list[4].parameters_list == ['**bar']


def test_should_return_filename_and_directory_from_code_file(extractor):
    methods_list = extractor.all_methods()

    assert methods_list[
        0].filename == os.getcwd() + '/tests/fixtures/my_python_test_file.py'


def test_ignore_self_from_parameter_list(os_mock, extractor):
    file_mock = mock.mock_open(read_data='def foo(self, bar):')
    with mock.patch('builtins.open', file_mock, create=True):
        methods_list = extractor.all_methods()

    assert methods_list[0].parameters_list == ['bar']


def test_ignore_cls_from_parameter_list(os_mock, extractor):
    file_mock = mock.mock_open(read_data='def foo(cls, bar):')
    with mock.patch('builtins.open', file_mock, create=True):
        methods_list = extractor.all_methods()

    assert methods_list[0].parameters_list == ['bar']


def test_ignore_default_values_of_parameters(os_mock, extractor):
    file_mock = mock.mock_open(
        read_data=
        'def send(self, request, stream=False, timeout=None, verify=True, cert=None, proxies=None):'
    )
    with mock.patch('builtins.open', file_mock, create=True):
        methods_list = extractor.all_methods()

    assert methods_list[0].parameters_list == [
        'request', 'stream', 'timeout', 'verify', 'cert', 'proxies'
    ]


def test_return_an_empty_list_when_just_an_ignored_parameter_is_found_on_parameter_list(
        os_mock, extractor):
    file_mock = mock.mock_open(read_data='def foo(self):')
    with mock.patch('builtins.open', file_mock, create=True):
        methods_list = extractor.all_methods()

    assert methods_list[0].parameters_list == []
