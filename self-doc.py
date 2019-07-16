# This is a funny little stab at the self-documenting code trope.
# @author Juha-Matti Santala / hamatti.org

import inspect
import re

FUNCTION_DECLARATION_PATTERN = r'^def .*\(.*\):$'

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
    index = source_code.index(definition) + 1

    new_source = source_code[:]
    if source_code[index].startswith('    """'):
        return False

    new_source.insert(index, f'    {docstring}')

    with open(filename, 'w') as source_file:
        source_file.write('\n'.join(new_source))

def self_documenting_sum(a, b):
    """Sums up integers."""
    document('"""Sums up integers."""')
    return a + b


self_documenting_sum(2,5)