import re


class Analyzer(object):

    def __init__(self, content):
        self.content = content

    def parameters(self):
        raw_parameters_list = re.findall(r'(\(.*\))', self.content)
        parameters_list = [parameters.replace(')', '').replace('(', '') for parameters in raw_parameters_list if parameters != '()']
        return parameters_list
