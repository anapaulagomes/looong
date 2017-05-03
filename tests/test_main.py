from looong import main
import os
import pytest
import mock
import argparse
from argparse import Namespace


@pytest.fixture()
def argparse_mock(mocker):
    parser = argparse.ArgumentParser()
    directory = Namespace(directory=os.getcwd() + '/tests/fixtures')
    yield mocker.patch('argparse.ArgumentParser.parse_args', return_value=directory)


def test_print_number_of_analyzed_files(capsys, argparse_mock):
    expected_report = """\nAnalyzed files: 1\nAnalyzed methods: 10\n\nfoooo [{}/tests/fixtures/my_python_test_file.py] ['bar', 'other_bar', 'barz', 'barzz', 'baroo'] \x1b[6;31;40m5\x1b[0m\nfooooo [{}/tests/fixtures/my_python_test_file.py] ['bar', 'other_bar', 'barz', 'barzz', 'baroo'] \x1b[6;31;40m5\x1b[0m\nfoooooo [{}/tests/fixtures/my_python_test_file.py] ['bar', 'other_bar', 'blabla', 'b'] \x1b[6;31;40m4\x1b[0m\n""".format(os.getcwd(), os.getcwd(), os.getcwd())

    main.execute()

    out, _ = capsys.readouterr()
    assert out == expected_report
