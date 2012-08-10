#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from collections import OrderedDict
import unittest
import sys
sys.path.append('../')
from jsonq import jsonq

class JsonqTestSuite(unittest.TestCase):
    """Jsonq Test cases."""

    def setUp(self):
        _str = '[{"k": "a", "v": 1}, {"k": "b", "v": 2}, {"k": "c", "v": 3}]'
        self.json = json.loads(_str, object_pairs_hook=OrderedDict)

    def test_select(self):
        obj = jsonq(self.json, {'select' : ['k', 'v']})
        self.assertEqual(list(obj), [['a', 1], ['b', 2], ['c', 3]])

    def test_filter(self):
        obj = jsonq(self.json, {'filter' : ['v > 1']})
        self.assertEqual(list(obj), [{'k' : 'b', 'v' : 2},
                                     {'k' : 'c', 'v' : 3}])

    def test_sort(self):
        obj = jsonq(self.json, {'sort' : 'v'})
        self.assertEqual(list(obj), self.json)

    def test_min(self):
        obj = jsonq(self.json, {'min' : 'v'})
        self.assertEqual(list(obj), [{'k' : 'a', 'v' : 1}])

    def test_max(self):
        obj = jsonq(self.json, {'max' : 'v'})
        self.assertEqual(list(obj), [{'k' : 'c', 'v' : 3}])

    def test_decr(self):
        obj = jsonq(self.json, {'decr' : ['v']})
        self.assertEqual(list(obj), [{'k' : 'a', 'v' : 0},
                                     {'k' : 'b', 'v' : 1},
                                     {'k' : 'c', 'v' : 2}])

    def test_incr(self):
        obj = jsonq(self.json, {'incr' : ['v']})
        self.assertEqual(list(obj), [{'k' : 'a', 'v' : 2},
                                     {'k' : 'b', 'v' : 3},
                                     {'k' : 'c', 'v' : 4}])


if __name__ == '__main__':
    unittest.main()

