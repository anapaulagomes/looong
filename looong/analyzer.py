from operator import attrgetter


class Analyzer(object):
    LONG_PARAMETER_THRESHOULD = 3

    def __init__(self, method_list):
        self.method_list = method_list

    def execute(self):
        ranking = self.long_parameter_list_ranking()

        for method in ranking:
            number_of_parameters = ('\x1b[6;31;40m{}\x1b[0m').format(len(method.parameters_list))
            print('{} [{}] {} {}'.format(method.name, method.filename, method.parameters_list, number_of_parameters))

    def has_long_parameter_list(self, method):
        return len(method.parameters_list) > self.LONG_PARAMETER_THRESHOULD

    def long_parameter_list_ranking(self):
        methods_with_long_parameter_list = list(filter(self.has_long_parameter_list, self.method_list))
        methods_with_long_parameter_list = sorted(methods_with_long_parameter_list, key=lambda method: len(method.parameters_list), reverse=True)
        return methods_with_long_parameter_list[:10]
