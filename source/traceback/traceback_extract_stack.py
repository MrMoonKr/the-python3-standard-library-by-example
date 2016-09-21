#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""
#end_pymotw_header

import traceback
import sys
import os

from traceback_example import call_function


def f():
    return traceback.extract_stack()


stack = call_function(f)
for filename, linenum, funcname, source in stack:
    print('{:<26}:{} {!r} in {}()'.format(
        os.path.basename(filename), linenum,
        source, funcname)
    )