from looong.analyzer import Analyzer


def test_identify_one_parameter_on_parameter_list():
    method_declaration_line = 'def foo(bar):'

    analyzer = Analyzer(method_declaration_line)

    parameters = analyzer.parameters()
    expected_parameters = ['bar']

    assert parameters == expected_parameters

def test_identify_multiple_parameters_on_parameter_list():
    method_declaration_line = 'def foo(bar, other_bar):'

    analyzer = Analyzer(method_declaration_line)

    parameters = analyzer.parameters()
    expected_parameters = ['bar', 'other_bar']

    assert parameters == expected_parameters

def test_should_return_empty_list_when_there_is_no_parameters_on_parameter_list():
    method_declaration_line = 'def foo():'

    analyzer = Analyzer(method_declaration_line)

    parameters = analyzer.parameters()
    expected_parameters = []

    assert parameters == expected_parameters
