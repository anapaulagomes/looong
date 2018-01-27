import os
from unittest import mock

from looong.extractor import Extractor


def test_return_method_with_one_parameter_when_method_has_one_parameter(
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


def test_should_return_method_with_an_empty_list_when_there_is_no_parameters(
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
        read_data='def send(self, request, stream=False, '
                  'timeout=None, verify=True, cert=None, proxies=None):'
    )
    with mock.patch('builtins.open', file_mock, create=True):
        methods_list = extractor.all_methods()

    assert methods_list[0].parameters_list == [
        'request', 'stream', 'timeout', 'verify', 'cert', 'proxies'
    ]


def test_return_an_empty_list_when_find_ignored_parameter_is_found(
        os_mock, extractor):
    file_mock = mock.mock_open(read_data='def foo(self):')
    with mock.patch('builtins.open', file_mock, create=True):
        methods_list = extractor.all_methods()

    assert methods_list[0].parameters_list == []


def test_should_skip_excluded_folders(mocker):
    extractor = Extractor('/bla')

    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('os.walk', return_value=[
            ('/bla/foo', ['venv', '.git', '__pycache__'], ()),
            ('/bla/foo/venv', ['bin', 'activate'], ('a.py', 'b.py')),
            ('/bla/foo/venv/bin', [], ('python', 'activate')),
            ('/bla/foo/.git', [], ('python', 'activate')),
            ('/bla/foo/node_modules', [], ('a.py', 'b.py')),
        ])

    methods_list = extractor.all_methods()

    assert methods_list == []


def test_should_skip_excluded_files(mocker):
    extractor = Extractor('/home/bla')

    mocker.patch('os.walk', return_value=[
            ('/home/bla/foo', [], []),
            ('/home/bla/foo/bar', ['x', 'z'], ['a.py', 'b.jar']),
            ('/home/bla/foo/x', [], ['python.pyc', 'noextension']),
            ('/home/bla/foo/z', [], ['python', 'activate']),
            ('/home/bla/foo/module', [], ['a.rb', 'b.py']),
        ])

    read_data = 'def foo(self, one, two, three, four):'
    file_mock = mock.mock_open(read_data=read_data)
    with mock.patch('builtins.open', file_mock, create=True):
        methods_list = extractor.all_methods()

    assert len(methods_list) == 2
