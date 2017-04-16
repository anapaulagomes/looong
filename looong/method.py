class Method(object):

    def __init__(self, name, filename, parameters):
        self._name = name
        self._filename = filename
        self._parameters = parameters

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @property
    def name(self):
        return self._name

    @property
    def filename(self):
        return self._filename

    @property
    def parameters_list(self):
        return self._parameters
