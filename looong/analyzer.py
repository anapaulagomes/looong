class Analyzer(object):

    def __init__(self, content):
        self.content = content

    def parameters(self):
        # TODO implement this with regex
        parenthesis_left_side = self.content.find('(')
        parenthesis_right_side = self.content.find(')')
        parameters = self.content[parenthesis_left_side+1:parenthesis_right_side]

        if parameters == '':
            return []
        else:
            return parameters.replace(' ', '').split(',')
