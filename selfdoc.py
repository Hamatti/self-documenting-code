# This is a funny little stab at the self-documenting code trope.
# @author Juha-Matti Santala / hamatti.org

from selfdocumenter import document

def self_documenting_sum(a, b):
    document('Sums up integers.')

    def foo(x, y):
        document('foooo')
        return x - y

    foo(1,2)
    return a + b


self_documenting_sum(2,5)