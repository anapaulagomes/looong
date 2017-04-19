from looong.method import Method
import re


class Extractor(object):

    def __init__(self, filename):
        self.filename = filename

    def methods(self):
        method_list = []

        raw_parameters_list = re.findall(r'def ([a-z]*)\((.*)\)', self.filename.read())

        for name, parameters in raw_parameters_list:
            parameters_list = parameters.replace(' ', '').split(',')
            method = Method(name, self.filename, [] if parameters_list[0] == '' else parameters_list)
            method_list.append(method)

        return method_list
