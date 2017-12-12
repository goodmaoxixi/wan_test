# -*- coding: utf-8 -*-

# The following sys.path management is under title
# 'PYTHONPATH, and finding packages & modules during development' in
# Structuring, Testing, and Maintaining Python Programs
# https://intermediate-and-advanced-software-carpentry.readthedocs.io/en/latest/structuring-python.html
import sys
import os

this_dir = os.path.dirname(__file__)
root_dir = os.path.abspath(os.path.join(this_dir, '..'))

# The path insertion guard as the C/C++ include guard.
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

import wantest
