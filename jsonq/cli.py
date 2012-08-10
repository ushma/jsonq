# -*- coding: utf-8 -*-
"""
jsonq.cli

Defines the command line parser
"""

import argparse
from . import __doc__, __title__

def _(_str):
    """Trim the white space."""
    return ' '.join(_str.strip().split())

parser = argparse.ArgumentParser(description=__doc__, prog=__title__)

parser.add_argument(
        '--filter',
        nargs='*', 
        help=_('''
            Condition option(s) to filter json.
        ''')
)
parser.add_argument(
        '--sort',
        help=_('''
            Sort the output accordingly based on the key, 
            works on ordered items like an array.
        ''')
)
parser.add_argument(
        '--min',
        help=_('''
            Print the record with the minimum key.
        ''')
)
parser.add_argument(
        '--max',
        help=_('''
            Print the record with the maximum key.
        ''')
)
parser.add_argument(
        '--decr',
        nargs='*',
        help=_('''
            Decrement the key(s).
        ''')
)
parser.add_argument(
        '--incr',
        nargs='*',
        help=_('''
            Increment the key(s).
        ''')
)
parser.add_argument(
        '--select',
        nargs='*', 
        help=_('''
            Collection of key(s) to be selected for the output.
        ''')
)
parser.add_argument(
        '--output',
        choices = ['compact', 'pretty', 'tabular'],
        default = 'pretty', 
        help=_('''Output mode can be changed to 'compact' or 'tabular' form. 
            The default mode is set to prettify 
            the json output 'pretty' with 2 space indent.
        ''')
)

