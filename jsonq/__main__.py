#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This main entry point.
Invoked as python -m jsonq

"""

from .cli import parser
from .core import jsonq
from .utils import isArr, isDict, isStr
import json
from collections import OrderedDict
import sys

def print_output(output, mode):
    _str = str
    if mode == 'compact':
        json.dump(list(output), sys.stdout)
        sys.stdout.write('\n')
    elif mode == 'tabular':
        _it = next(output)
        if isDict(_it):
            print '\t'.join(map(_str, _it.itervalues()))
            for v in output:
                print '\t'.join(map(_str, v.itervalues()))
        elif isArr(_it):
            print '\t'.join(map(_str, _it))
            for obj in output:
                print '\t'.join(map(_str, obj))
        elif isStr(_it):
            print _it
            for obj in output:
                print obj
    elif mode == 'pretty':
        json.dump(list(output), sys.stdout, indent=2)
        sys.stdout.write('\n')

def main():
    args = vars(parser.parse_args())
    valid_args = dict([(k, v) for k, v in args.iteritems() if v is not None])
    json_obj = json.load(sys.stdin, object_pairs_hook=OrderedDict)
    output = jsonq(json_obj, valid_args)
    print_output(output, args['output'])

if __name__ == '__main__':
    main()
    

