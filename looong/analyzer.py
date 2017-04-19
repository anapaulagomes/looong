from operator import attrgetter


class Analyzer(object):

    def __init__(self, method_list):
        self.method_list = method_list

    def top_parameter_list(self):
        return max(self.method_list, key=attrgetter('parameters_list'))
