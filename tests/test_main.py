import os
from argparse import Namespace

import pytest

from looong import main


@pytest.fixture()
def argparse_mock(mocker):
    directory = Namespace(directory=os.getcwd() + '/tests/fixtures')
    yield mocker.patch(
        'argparse.ArgumentParser.parse_args', return_value=directory)


def test_print_number_of_analyzed_files(capsys, argparse_mock):
    expected_output = "\nAnalyzed files: 1\nAnalyzed methods: 10\n\n" \
                      "foooo [{}/tests/fixtures/my_python_test_file.py] " \
                      "['bar', 'other_bar', 'barz', 'barzz', 'baroo'] \x1b" \
                      "[6;31;40m5\x1b[0m\nfooooo " \
                      "[{}/tests/fixtures/my_python_test_file.py] " \
                      "['bar', 'other_bar', 'barz', 'barzz', 'baroo'] " \
                      "\x1b[6;31;40m5\x1b[0m\nfoooooo " \
                      "[{}/tests/fixtures/my_python_test_file.py] " \
                      "['bar', 'other_bar', 'blabla', 'b'] " \
                      "\x1b[6;31;40m4\x1b[0m\n"
    expected_report = expected_output.format(
        os.getcwd(), os.getcwd(), os.getcwd())

    main.execute()

    out, _ = capsys.readouterr()
    assert out == expected_report
