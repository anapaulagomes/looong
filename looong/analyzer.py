from operator import attrgetter


class Analyzer(object):
    LONG_PARAMETER_THRESHOULD = 3

    def __init__(self, method_list):
        self.method_list = method_list

    def has_long_parameter_list(self, method):
        return len(method.parameters_list) > self.LONG_PARAMETER_THRESHOULD

    def long_parameter_list_ranking(self):
        methods_with_long_parameter_list = list(filter(self.has_long_parameter_list, self.method_list))
        methods_with_long_parameter_list = sorted(methods_with_long_parameter_list, key=lambda method: len(method.parameters_list), reverse=True)
        return methods_with_long_parameter_list[:10]
