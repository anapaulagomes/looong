from looong.method import Method
import re
import os


class Extractor(object):

    def __init__(self, directory):
        self.directory = directory

    def all_methods(self):
        full_directory = self.directory
        methods_list = []

        for dirpath, dirnames, filenames in os.walk(full_directory):
            for filename in filenames:
                filename_with_path = dirpath + '/' + filename
                methods_list = methods_list + self.__methods(filename_with_path)

        return methods_list

    def __methods(self, filename):
        method_list = []
        filename = open(filename, encoding='ISO-8859-1')# TODO verify the better way to get the encoding
        raw_parameters_list = self.__identify_method_patterns(filename)

        for name, parameters in raw_parameters_list:
            parameters_list = self.__clean_parameters(parameters)

            if parameters_list != []:
                method = Method(name, filename.name, [] if parameters_list[0] == '' else parameters_list)
            else:
                method = Method(name, filename.name, [])
            method_list.append(method)

        return method_list

    def __identify_method_patterns(self, filename):
        return re.findall(r'def ([a-z]*)\((.*)\)', filename.read())

    def __clean_parameters(self, raw_parameters_list):
        parameters_list = raw_parameters_list.replace(' ', '').split(',')
        parameters_list = self.__ignored_parameters(parameters_list)
        parameters_list = self.__ignore_default_values(parameters_list)
        return parameters_list

    def __ignored_parameters(self, parameters_list):
        ignored_parameters = ['self', 'cls']
        return [parameter for parameter in parameters_list if parameter not in ignored_parameters]

    def __ignore_default_values(self, parameters_list):
        return [parameter[:parameter.find('=')] if parameter.find('=') != -1 else parameter for parameter in parameters_list]
