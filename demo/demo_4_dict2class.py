#!python
# -*- coding: utf-8 -*-
'''
@File: demo_4_dict2class.py
@Date: 2023/05/07 09:54:18
@Author: Baoming Yu (bayu)
@Version: 1.0
@Description: None
'''

import datetime
import os
import sys

sys.path.append(os.getcwd())
from pygadget import Dict2Class

def demo(argv=None):
    test_dict = {
        'now': datetime.datetime.now(),
        'num': 77,
        'txt': 'Hello!',
        'dct': {
            't_num': 667,
            't_txt': 'hello!'
        },
        'lst': [1, 2, 3, 'abc', {'inner': 'world'}, [9, 8, {'more_inner': 'inside'}]], # need refine
        'set': {1, 3, 3, 4, 'abc'},
        'tpl': (1, 2, 3, 5, 'abc', {'inner': 'world'})
    }
    
    ud_class = Dict2Class().convert(test_dict)

    ud_class_with_recursive = Dict2Class().convert(test_dict, recursive=True)
    pass


if __name__ == '__main__':
    demo()

