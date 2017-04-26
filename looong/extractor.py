from looong.method import Method
from looong.codefile import CodeFile
import re
import os


class Extractor(object):

    def __init__(self, directory):
        self.directory = directory

    def code_files(self):
        full_directory = os.getcwd() + self.directory
        code_files_list = []

        for dirpath, dirnames, filenames in os.walk(full_directory):
            for filename in filenames:
                filename_with_path = dirpath + '/' + filename
                method_list = self.__methods(filename_with_path)
                code_file = CodeFile(filename, dirpath, method_list)
                code_files_list.append(code_file)

        return code_files_list

    def __methods(self, filename):
        method_list = []
        filename = open(filename)
        raw_parameters_list = re.findall(r'def ([a-z]*)\((.*)\)', filename.read())

        for name, parameters in raw_parameters_list:
            parameters_list = parameters.replace(' ', '').split(',')
            method = Method(name, filename, [] if parameters_list[0] == '' else parameters_list)
            method_list.append(method)

        return method_list
