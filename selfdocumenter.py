import inspect
import re

FUNCTION_DECLARATION_PATTERN = r'^(\s*)def .*\(.*\):\s*$'
EXTRA_SPACES = 4 * ' '


def document(docstring):
    function_name = inspect.stack()[1][3]
    filename = inspect.stack()[1][1]

    with open(filename, 'r') as source_file:
        source_code = source_file.read().split('\n')

    definitions = [line for line in source_code if re.match(FUNCTION_DECLARATION_PATTERN, line)]
    definition = [definition for definition in definitions if function_name in definition]
    if not definition:
        return False

    definition = definition[0]

    indentation_level = f'{re.match(FUNCTION_DECLARATION_PATTERN, definition).groups()[0]}{EXTRA_SPACES}'

    index = source_code.index(definition) + 1

    new_source = source_code[:]

    docstring_pattern = r'^\s*"""' + docstring + '"""\s*$'
    if re.match(docstring_pattern,source_code[index]):
        return False

    new_source.insert(index, f'{indentation_level}"""{docstring}"""')

    # Remove original document line
    document_call_pattern = r'^\s*document\(\'' + docstring + '\'\)\s*$'
    new_source = [line for line in new_source if not re.match(document_call_pattern, line)]

    with open(filename, 'w') as source_file:
        source_file.write('\n'.join(new_source))