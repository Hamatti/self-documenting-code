import inspect
import re

FUNCTION_DECLARATION_PATTERN = r'^(\s*)def .*\(.*\):\s*$'
EXTRA_SPACES = 4 * ' '


def document(docstring):
    """Please note, never actually use this. This is part of a joke.

    This function modifies the source code of the file that calls this function. It does two things to the source code:

    1) It adds docstring with triple quotes as the first line in function body if docstring does not exist yet.
    2) It removes the call to this function."""

    # Reach into stack to see what the calling function is called and which file it is from
    caller_function_name = inspect.stack()[1][3]
    caller_filename = inspect.stack()[1][1]

    with open(caller_filename, 'r') as source_file:
        source_code = source_file.read().split('\n')

    # Find the correct function definition that this function was called from in the source code
    function_definitions = [line for line in source_code if re.match(FUNCTION_DECLARATION_PATTERN, line)]
    try:
        caller_function_definition = [definition for definition in function_definitions if caller_function_name in definition][0]
    except IndexError:
        return False

    # Hardcoded indentation of 4 spaces is added (compared to the function definition line)
    new_indentation_spaces = f'{re.match(FUNCTION_DECLARATION_PATTERN, caller_function_definition).groups()[0]}{EXTRA_SPACES}'

    # Find out the right position for docstring in source code
    index = source_code.index(caller_function_definition) + 1

    # See if docstring already exists and fail the function if it does
    docstring = docstring.replace('"', r'\"')
    docstring_pattern = r'^\s*"""' + docstring + '"""\s*$'
    if re.match(docstring_pattern, source_code[index]):
        return False

    # Add docstring to correct position with indentation
    source_code.insert(index, f'{new_indentation_spaces}"""{docstring}"""')

    # Remove original document line because it has filled its purpose
    document_call_pattern = r'^\s*document\(\'' + docstring + '\'\)\s*$'
    source_code = [line for line in source_code if not re.match(document_call_pattern, line)]

    with open(caller_filename, 'w') as source_file:
        source_file.write('\n'.join(source_code))

