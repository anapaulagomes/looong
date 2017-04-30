from operator import attrgetter


class Analyzer(object):
    LONG_PARAMETER_THRESHOULD = 3

    def __init__(self, method_list):
        self.method_list = method_list

    def has_long_parameter_list(self, method):
        return len(method.parameters_list) > self.LONG_PARAMETER_THRESHOULD

    def long_parameter_list_ranking(self):
        pass
