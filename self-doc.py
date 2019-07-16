# This is a funny little stab at the self-documenting code trope.
# @author Juha-Matti Santala / hamatti.org

from selfdocumenter import document

def self_documenting_sum(a, b):
    """Sums up integers."""
    document('"""Sums up integers."""')
    return a + b


self_documenting_sum(2,5)