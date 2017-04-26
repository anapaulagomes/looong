class CodeFile(object):

    def __init__(self, filename, directory, method_list):
        self._filename = filename
        self._directory = directory
        self._method_list = method_list

    @property
    def filename(self):
        return self._filename

    @property
    def directory(self):
        return self._directory

    @property
    def method_list(self):
        return self._method_list
