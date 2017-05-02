from extractor import Extractor
from analyzer import Analyzer
import os
from optparse import OptionParser


def capture_options():
    parser = OptionParser()
    parser.add_option("-d", "--directory", dest="directory", default=os.getcwd(), help="the project directory to analyze")
    (options, args) = parser.parse_args()
    return options


def extract_all_methods(directory):
    extractor = Extractor(directory)
    all_methods = extractor.all_methods()

    method_list = set(method.filename for method in all_methods)

    print('\nAnalyzed files: {}'.format(len(method_list)))
    return all_methods


def analyze(all_methods):
    method_list = [method for method in all_methods]
    print('Analyzed methods: {}\n'.format(len(method_list)))
    analyzer = Analyzer(method_list)
    analyzer.execute()

if __name__ == '__main__':
    options = capture_options()
    directory = options.directory
    code_files = extract_all_methods(directory)
    analyze(code_files)
