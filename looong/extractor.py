from looong.method import Method
import re


class Extractor(object):

    def __init__(self, filename):
        self.filename = filename

    def methods(self):
        parameters_list = self._parameters()
        return [Method('foo', 'foo.py', parameters_list)]

    def _parameters(self):
        raw_parameters_list = re.findall(r'(\(.*\))', self.filename.read())
        parameters_list = [parameters.replace(')', '').replace('(', '') for parameters in raw_parameters_list if parameters != '()']
        return parameters_list
