import os

import pytest

from looong.extractor import Extractor
from looong.method import Method


@pytest.fixture
def method_list():
    method1 = Method('foo', 'my_python_test_file.py',
                     ['bar', 'other_bar', 'other_bar_barz'])
    method2 = Method('fooo', 'my_python_test_file.py',
                     ['bar', 'other_bar', 'other_bar_barz', 'bazz'])
    method3 = Method('foooo', 'my_python_test_file.py', [
        'bar', 'other_bar', 'bar_plus_bar', 'other_bar_barz', 'baz', 'bazz'
    ])
    method4 = Method('fooooo', 'my_python_test_file.py', ['bar', 'other_bar'])
    method5 = Method('bar', 'my_python_test_file.py',
                     ['bar', 'other_bar', 'other_bar_barz', 'baz', 'bazz'])
    method6 = Method('barbar', 'my_python_test_file.py', [
        'bar', 'other_bar', 'bar_plus_bar', 'other_bar_barz', 'baz'
    ])
    return [method1, method2, method3, method4, method5, method6]


@pytest.fixture
def method_list_with_10_long_parameter_list():
    return [
        Method('foo', 'my_python_test_file.py',
               ['bar', 'other_bar', 'other_bar_barz']),
        Method('fooo', 'my_python_test_file.py',
               ['bar', 'other_bar', 'other_bar_barz', 'bazz']),
        Method('foooo', 'my_python_test_file.py', [
            'bar', 'other_bar', 'bar_plus_bar', 'other_bar_barz', 'baz', 'bazz'
        ]),
        Method('fooooo', 'my_python_test_file.py', ['bar', 'other_bar']),
        Method('bar', 'my_python_test_file.py',
               ['bar', 'other_bar', 'other_bar_barz', 'baz', 'bazz']),
        Method('barbar', 'my_python_test_file.py',
               ['bar', 'other_bar', 'bar_plus_bar', 'other_bar_barz', 'baz']),
        Method('foooo', 'my_python_test_file.py', [
            'bar', 'other_bar', 'bar_plus_bar', 'other_bar_barz', 'baz', 'bazz'
        ]),
        Method('fooooo', 'my_python_test_file.py', ['bar', 'other_bar']),
        Method('bar', 'my_python_test_file.py',
               ['bar', 'other_bar', 'other_bar_barz', 'baz', 'bazz']),
        Method('barbar', 'my_python_test_file.py',
               ['bar', 'other_bar', 'bar_plus_bar', 'other_bar_barz', 'baz']),
        Method('foooo', 'my_python_test_file.py', [
            'bar', 'other_bar', 'bar_plus_bar', 'other_bar_barz', 'baz', 'bazz'
        ]),
        Method('fooooo', 'my_python_test_file.py', ['bar', 'other_bar']),
        Method('bar', 'my_python_test_file.py',
               ['bar', 'other_bar', 'other_bar_barz', 'baz', 'bazz']),
        Method('barbar', 'my_python_test_file.py',
               ['bar', 'other_bar', 'bar_plus_bar', 'other_bar_barz', 'baz']),
        Method('barbar', 'my_python_test_file.py',
               ['bar', 'other_bar', 'bar_plus_bar', 'other_bar_barz', 'baz']),
        Method('foooo', 'my_python_test_file.py', [
            'bar', 'other_bar', 'bar_plus_bar', 'other_bar_barz', 'baz', 'bazz'
        ]),
        Method('fooooo', 'my_python_test_file.py', ['bar', 'other_bar']),
        Method('bar', 'my_python_test_file.py',
               ['bar', 'other_bar', 'other_bar_barz', 'baz', 'bazz']),
        Method('barbar', 'my_python_test_file.py',
               ['bar', 'other_bar', 'bar_plus_bar', 'other_bar_barz', 'baz'])
    ]


@pytest.fixture()
def os_mock(mocker):
    directory = '/tests/fixtures'
    mocker.patch('os.getcwd', return_value='/home/bla')
    yield mocker.patch('os.walk', return_value=[(directory, [], ['foo.py'])])


@pytest.fixture()
def extractor():
    yield Extractor(os.getcwd() + '/tests/fixtures')
