from looong.extractor import Extractor
from looong.analyzer import Analyzer
import os
import argparse


def capture_options():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--directory",
        dest="directory",
        default=os.getcwd(),
        help="the project directory to analyze")

    args = parser.parse_args()
    return args


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


def execute():
    options = capture_options()
    directory = options.directory
    code_files = extract_all_methods(directory)
    analyze(code_files)


if __name__ == '__main__':
    execute()
