from looong.analyzer import Analyzer
from looong.method import Method
import os


def test_return_true_when_method_is_detected_with_long_parameter_list():
    method = Method('foo', 'my_python_test_file.py', ['self', 'bar', 'other_bar', 'other_bar_barz'])
    analyzer = Analyzer([])

    assert True is analyzer.has_long_parameter_list(method)


def test_return_false_when_method_is_detected_with_long_parameter_list():
    method = Method('foo', 'my_python_test_file.py', ['self', 'bar'])
    analyzer = Analyzer([])

    assert False is analyzer.has_long_parameter_list(method)


def test_return_same_method_when_ranking_with_one_method_with_long_parameter_list():
    method_list = [Method('fooo', 'my_python_test_file.py', ['bar', 'other_bar', 'other_bar_barz', 'baz', 'bazz'])]
    analyzer = Analyzer(method_list)
    ranking = analyzer.long_parameter_list_ranking()

    assert 1 == len(ranking)
    assert ranking[0] == Method('fooo', 'my_python_test_file.py', ['bar', 'other_bar', 'other_bar_barz', 'baz', 'bazz'])


def test_do_ranking_with_top_long_parameter_list():
    method_list = [ Method('foo', 'my_python_test_file.py', ['bar', 'other_bar', 'other_bar_barz']),
                    Method('fooo', 'my_python_test_file.py', ['bar', 'other_bar', 'other_bar_barz', 'bazz']),
                    Method('foooo', 'my_python_test_file.py', ['bar', 'other_bar', 'bar_plus_bar', 'other_bar_barz', 'baz', 'bazz']),
                    Method('fooooo', 'my_python_test_file.py', ['bar', 'other_bar']),
                    Method('bar', 'my_python_test_file.py', ['bar', 'other_bar', 'other_bar_barz', 'baz', 'bazz']),
                    Method('barbar', 'my_python_test_file.py', ['bar', 'other_bar', 'bar_plus_bar', 'other_bar_barz', 'baz'])]
    analyzer = Analyzer(method_list)
    ranking = analyzer.long_parameter_list_ranking()

    assert 4 == len(ranking)
    assert ranking[0] == Method('foooo', 'my_python_test_file.py', ['bar', 'other_bar', 'bar_plus_bar', 'other_bar_barz', 'baz', 'bazz'])
    assert ranking[1] == Method('bar', 'my_python_test_file.py', ['bar', 'other_bar', 'other_bar_barz', 'baz', 'bazz'])
    assert ranking[2] == Method('barbar', 'my_python_test_file.py', ['bar', 'other_bar', 'bar_plus_bar', 'other_bar_barz', 'baz'])
    assert ranking[3] == Method('fooo', 'my_python_test_file.py', ['bar', 'other_bar', 'other_bar_barz', 'bazz'])


def test_do_ranking_with_top_10_long_parameter_list():
    method_list = [ Method('foo', 'my_python_test_file.py', ['bar', 'other_bar', 'other_bar_barz']),
                    Method('fooo', 'my_python_test_file.py', ['bar', 'other_bar', 'other_bar_barz', 'bazz']),
                    Method('foooo', 'my_python_test_file.py', ['bar', 'other_bar', 'bar_plus_bar', 'other_bar_barz', 'baz', 'bazz']),
                    Method('fooooo', 'my_python_test_file.py', ['bar', 'other_bar']),
                    Method('bar', 'my_python_test_file.py', ['bar', 'other_bar', 'other_bar_barz', 'baz', 'bazz']),
                    Method('barbar', 'my_python_test_file.py', ['bar', 'other_bar', 'bar_plus_bar', 'other_bar_barz', 'baz']),
                    Method('foooo', 'my_python_test_file.py', ['bar', 'other_bar', 'bar_plus_bar', 'other_bar_barz', 'baz', 'bazz']),
                    Method('fooooo', 'my_python_test_file.py', ['bar', 'other_bar']),
                    Method('bar', 'my_python_test_file.py', ['bar', 'other_bar', 'other_bar_barz', 'baz', 'bazz']),
                    Method('barbar', 'my_python_test_file.py', ['bar', 'other_bar', 'bar_plus_bar', 'other_bar_barz', 'baz']),
                    Method('foooo', 'my_python_test_file.py', ['bar', 'other_bar', 'bar_plus_bar', 'other_bar_barz', 'baz', 'bazz']),
                    Method('fooooo', 'my_python_test_file.py', ['bar', 'other_bar']),
                    Method('bar', 'my_python_test_file.py', ['bar', 'other_bar', 'other_bar_barz', 'baz', 'bazz']),
                    Method('barbar', 'my_python_test_file.py', ['bar', 'other_bar', 'bar_plus_bar', 'other_bar_barz', 'baz']),
                    Method('barbar', 'my_python_test_file.py', ['bar', 'other_bar', 'bar_plus_bar', 'other_bar_barz', 'baz']),
                    Method('foooo', 'my_python_test_file.py', ['bar', 'other_bar', 'bar_plus_bar', 'other_bar_barz', 'baz', 'bazz']),
                    Method('fooooo', 'my_python_test_file.py', ['bar', 'other_bar']),
                    Method('bar', 'my_python_test_file.py', ['bar', 'other_bar', 'other_bar_barz', 'baz', 'bazz']),
                    Method('barbar', 'my_python_test_file.py', ['bar', 'other_bar', 'bar_plus_bar', 'other_bar_barz', 'baz'])]
    analyzer = Analyzer(method_list)
    ranking = analyzer.long_parameter_list_ranking()

    assert 10 == len(ranking)


def test_when_execute_show_method_filename_parameters_and_number_of_parameters(capsys):
    method_list = [Method('fooo', 'my_python_test_file.py', ['bar', 'other_bar', 'other_bar_barz', 'baz', 'bazz'])]
    analyzer = Analyzer(method_list)
    ranking = analyzer.execute()
    expected_message = '{} [{}] {} \x1b[6;31;40m{}\x1b[0m\n'.format('fooo', 'my_python_test_file.py', ['bar', 'other_bar', 'other_bar_barz', 'baz', 'bazz'], 5)

    out, err = capsys.readouterr()
    assert expected_message == out
