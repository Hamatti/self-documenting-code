def self_documenting_sum(a, b):
    """Sums up two integers"""
    with open(__file__, 'r') as source:
        data = source.read().split('\n')

    with open(__file__, 'w') as source:
        if not data[1].startswith('    "'):
            documentation = '    """Sums up two integers"""'
            new_source = data[:]
            new_source.insert(1, documentation)
            source.write('\n'.join(new_source))
        else:
            source.write('\n'.join(data))
    return a + b


self_documenting_sum(2,5)