from looong.analyzer import Analyzer
from looong.method import Method


def test_return_true_when_method_is_detected_with_long_parameter_list():
    method = Method('foo', 'my_python_test_file.py',
                    ['self', 'bar', 'other_bar', 'other_bar_barz'])
    analyzer = Analyzer([])

    assert analyzer.has_long_parameter_list(method)


def test_return_false_when_method_is_detected_with_long_parameter_list():
    method = Method('foo', 'my_python_test_file.py', ['self', 'bar'])
    analyzer = Analyzer([])

    assert not analyzer.has_long_parameter_list(method)


def test_return_same_method_when_ranking_one_method_with_long_parameter_list():
    method_list = [
        Method('fooo', 'my_python_test_file.py',
               ['bar', 'other_bar', 'other_bar_barz', 'baz', 'bazz'])
    ]
    analyzer = Analyzer(method_list)
    ranking = analyzer.long_parameter_list_ranking()

    assert len(ranking) == 1
    assert Method('fooo', 'my_python_test_file.py',
                  ['bar', 'other_bar', 'other_bar_barz', 'baz',
                   'bazz']) == ranking[0]


def test_do_ranking_with_top_long_parameter_list(method_list):
    analyzer = Analyzer(method_list)
    ranking = analyzer.long_parameter_list_ranking()

    assert len(ranking) == 4
    assert method_list[2] == ranking[0]
    assert method_list[4] == ranking[1]
    assert method_list[5] == ranking[2]
    assert method_list[1] == ranking[3]


def test_do_ranking_with_top_10_long_parameter_list(
        method_list_with_10_long_parameter_list):
    analyzer = Analyzer(method_list_with_10_long_parameter_list)
    ranking = analyzer.long_parameter_list_ranking()

    assert len(ranking) == 10


def test_when_execute_show_method_filename_parameters_and_number_of_parameters(
        capsys):
    method_list = [
        Method('fooo', 'my_python_test_file.py',
               ['bar', 'other_bar', 'other_bar_barz', 'baz', 'bazz'])
    ]
    analyzer = Analyzer(method_list)
    analyzer.execute()
    expected_message = '{} [{}] {} \x1b[6;31;40m{}\x1b[0m\n'.format(
        'fooo', 'my_python_test_file.py',
        ['bar', 'other_bar', 'other_bar_barz', 'baz', 'bazz'], 5)

    out, err = capsys.readouterr()
    assert out == expected_message
