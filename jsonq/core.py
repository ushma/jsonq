# -*- coding: utf-8 -*-

"""
jsonq.core

Contains the core processing functions.

"""

from .utils import isArr, isDict
from itertools import imap
from operator import itemgetter
import string
import re

__all__ = ('jsonq')
_orderfn = ('filter',
            'sort',
            'min',
            'max',
            'decr',
            'incr',
            'select')
_min = min
_max = max
operators = {'<' : -1,
             '==' : 0,
             '>' : 1}
parseOpRe = re.compile(r'(<|==|>)')

def _(_str):
    """Remove the white space."""
    return ''.join(_str.strip().split())

def select(iterable, args):
    if len(args) == 1:
        for obj in iterable:
            yield obj[args[0]]
    else:
        for obj in iterable:
             yield [v for k, v in obj.iteritems() if k in args]   

def filter(iterable, args):
    _it = iterable
    parse_op = imap(parseOpRe.split, imap(_, args))
    for (k, op, v) in parse_op:
        op_cmp = operators[op]
        v = int(v)
        _it = (obj for obj in _it if obj[k].__cmp__(v) == op_cmp)
    return _it 

def sort(iterable, key):
    return iter(sorted(iterable, key=itemgetter(key)))  

def min(iterable, key):
    yield _min(iterable, key=itemgetter(key))

def max(iterable, key):
    yield _max(iterable, key=itemgetter(key))

def decr(iterable, args):
    for obj in iterable:
        for k in args:
            obj[k] -= 1
        yield obj

def incr(iterable, args):
    for obj in iterable:
        for k in args:
            obj[k] += 1
        yield obj

def jsonq(json_obj, options):
    functions = globals()
    # get an ordered chain of functions to be processed
    chain = [(functions[fn], options[fn]) for fn in _orderfn if fn in options]
    _it = json_obj
    if isDict(_it):
        _it = [_it]
    for fn, args in chain:
        _it = fn(_it, args)
    return _it

