# This is a funny little stab at the self-documenting code trope.
# @author Juha-Matti Santala / hamatti.org

import inspect
import re

FUNCTION_DECLARATION_PATTERN = r'^def .*\(.*\):$'

def document(fn, docstring):

    # Read source
    with open(__file__, 'r') as source_file:
        source_code = source_file.read().split('\n')

    # Find the right function declaration
    definitions = [line for line in source_code if re.match(FUNCTION_DECLARATION_PATTERN, line)]
    definition = [definition for definition in definitions if fn in definition]
    if not definition:
        return False

    definition = definition[0]
    index = source_code.index(definition) + 1

    # Insert docstring
    new_source = source_code[:]
    if(source_code[index].startswith('    """')):
        return False

    new_source.insert(index, docstring)

    # Write back to file
    with open(__file__, 'w') as source_file:
        source_file.write('\n'.join(new_source))

def self_documenting_sum(a, b):
    document(inspect.stack()[0][3], '    """Sums up integers."""')
    return a + b


self_documenting_sum(2,5)