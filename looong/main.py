from extractor import Extractor
from analyzer import Analyzer


extractor = Extractor('/django-master')
code_files = extractor.code_files()
print('Analyzed files: {}'.format(len(code_files)))

method_list = []

for code in code_files:
    for method in code.method_list:
        method_list.append(method)

print('Analyzed methods: {}'.format(len(method_list)))
analyzer = Analyzer(method_list)
analyzer.execute()
