=====
jsonq
=====

**jsonq** provides a simple and easy to use 
command line utility to process json with linq.
It traverses through the JSON object, processes it
as per linq rules specified and produces
another JSON object or a line based format which
can be processed by other linux utilities. 
The input is an array of objects similar to  
a collection of database records.
It also provides an interface to be directly used 
and imported in python.

Usage
=====

Examples
--------
::

    $ cat example.json
    [{"k": "a", "v": 1}, {"k": "b", "v": 2}, {"k": "c", "v": 3}] 

select
------
::

    $ cat example.json | jsonq --select k v
    [
      [
        "a", 
        1
      ], 
      [
        "b", 
        2
      ], 
      [
        "c", 
        3
      ]
    ]  

filter
------
::

    $ cat example.json | jsonq --filter 'v>1'
    [
      {
        "k": "b", 
        "v": 2
      }, 
      {
        "k": "c", 
        "v": 3
      }
    ] 

sort
----
::

    $ cat example.json | jsonq --sort v
    [
      {
        "k": "a", 
        "v": 1
      }, 
      {
        "k": "b", 
        "v": 2
      }, 
      {
        "k": "c", 
        "v": 3
      }
    ] 

min
---
::

    $ cat example.json | jsonq --min v
    [
      {
        "k": "a", 
        "v": 1
      }
    ]  

max
---
::

    $ cat example.json | jsonq --max v
    [
      {
        "k": "c", 
        "v": 3
      }
    ]  

decr
----
::

    $ cat example.json | jsonq --decr v
    [
      {
        "k": "a", 
        "v": 0
      }, 
      {
        "k": "b", 
        "v": 1
      }, 
      {
        "k": "c", 
        "v": 2
      }
    ] 

incr
----
::

    $ cat example.json | jsonq --incr v
    [
      {
        "k": "a", 
        "v": 2
      }, 
      {
        "k": "b", 
        "v": 3
      }, 
      {
        "k": "c", 
        "v": 4
      }
    ] 

output
------
Output mode can be changed to compact or pretty JSON(with indentation of 2) mode.
A line based output can also be produced.::

    $ cat example.json | jsonq --select k v --output tabular
    a       1
    b       2
    c       3 


Python API
----------

jsonq can be imported as a generator in python::

    >>> from jsonq import jsonq
    >>> obj = [{"k": "a", "v": 1}, {"k": "b", "v": 2}, {"k": "c", "v": 3}]
    >>> for _obj in jsonq(obj, {'select' : ['k', 'v']}):
    ...     print _obj
    ... 
    ['a', 1]
    ['b', 2]
    ['c', 3]      
    

To parse JSON::

    >>> import json
    >>> from collections import OrderedDict
    >>> obj = json.loads('[{"k": "a", "v": 1}, {"k": "b", "v": 2}, {"k": "c", "v": 3}]', 
    ...                     object_pairs_hook=OrderedDict)

``object_pairs_hook`` option can be used to maintain the object keys order.


Flags
-----

``$ jsonq --help``::

    usage: jsonq [-h] [--filter [FILTER [FILTER ...]]] [--sort SORT] [--min MIN]
                 [--max MAX] [--decr [DECR [DECR ...]]] [--incr [INCR [INCR ...]]]
                 [--select [SELECT [SELECT ...]]]
                 [--output {compact,pretty,tabular}]

    jsonq - query for json

    optional arguments:
      -h, --help            show this help message and exit
      --filter [FILTER [FILTER ...]]
                            Condition option(s) to filter json.
      --sort SORT           Sort the output accordingly based on the key, works on
                            ordered items like an array.
      --min MIN             Print the record with the minimum key.
      --max MAX             Print the record with the maximum key.
      --decr [DECR [DECR ...]]
                            Decrement the key(s).
      --incr [INCR [INCR ...]]
                            Increment the key(s).
      --select [SELECT [SELECT ...]]
                            Collection of key(s) to be selected for the output.
      --output {compact,pretty,tabular}
                            Output mode can be changed to 'compact' or 'tabular'
                            form. The default mode is set to prettify the json
                            output 'pretty' with 2 space indent.


