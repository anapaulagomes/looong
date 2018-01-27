from looong.method import Method
import re
import os


EXCLUDED_DIRS = [
    'tests',
    'node_modules',
    'bower_components',
]

EXCLUDED_FILES = [
    'conftest.py'
]


class Extractor(object):
    def __init__(self, directory):
        self.directory = directory
        EXCLUDED_DIRS.append(os.environ.get('VIRTUAL_ENV', None))

    def all_methods(self):
        methods_list = []

        for current_folder, dirs, files in os.walk(self.directory, topdown=True):
            if self._is_virtual_env(current_folder):
                dirs[:] = []
                continue

            dirs[:] = self._allowed_dirs(dirs)
            files[:] = self._allowed_files(files)

            for filename in files:
                filename_with_path = current_folder + '/' + filename
                methods_list = methods_list + self._methods(filename_with_path)

        return methods_list

    def _allowed_dirs(self, dirs):
        return [directory for directory in dirs
                if directory not in EXCLUDED_DIRS and
                not directory.startswith('.') and
                not directory.startswith('_')]

    def _allowed_files(self, files):
        return [dfile
                for dfile in files
                if dfile not in EXCLUDED_FILES and
                dfile.lower().endswith('.py')]

    def _methods(self, filename):
        method_list = []
        filename = open(
            filename, encoding='ISO-8859-1'
        )  # TODO verify the better way to get the encoding
        raw_parameters_list = self._identify_method_patterns(filename)

        for name, parameters in raw_parameters_list:
            parameters_list = self._clean_parameters(parameters)

            if parameters_list:
                method = Method(name, filename.name, [] if
                                parameters_list[0] == '' else parameters_list)
            else:
                method = Method(name, filename.name, [])
            method_list.append(method)

        return method_list

    def _identify_method_patterns(self, filename):
        return re.findall(r'def ([a-z]*)\((.*)\)', filename.read())

    def _clean_parameters(self, raw_parameters_list):
        parameters_list = raw_parameters_list.replace(' ', '').split(',')
        parameters_list = self._ignored_parameters(parameters_list)
        parameters_list = self._ignore_default_values(parameters_list)
        return parameters_list

    def _ignored_parameters(self, parameters_list):
        ignored_parameters = ['self', 'cls']
        return [
            parameter for parameter in parameters_list
            if parameter not in ignored_parameters
        ]

    def _ignore_default_values(self, parameters_list):
        return [
            parameter[:parameter.find('=')]
            if parameter.find('=') != -1 else parameter
            for parameter in parameters_list
        ]

    def _is_virtual_env(self, current_folder):
        python = os.path.exists(current_folder + '/bin/python')
        activate = os.path.exists(current_folder + '/bin/activate')

        return python or activate
