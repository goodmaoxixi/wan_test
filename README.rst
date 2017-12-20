WAN Test Suite
====================

A WAN test suite which simplifies the boring WAN test work with automatic schedule tasks.

Features Implemented
-----------------------------
1. ping
2. nslookup
3. portal retrieval
4. mail sending with or without a proxy

Features to Be Implemented
-----------------------------
1. Formatted output, e.g., CSV format, Excel format
2. schedule tasks, and more

Configuration File
-----------------------------
wan_test.ini, which holds all the input info. 

Ouput
-----------------------------
All the outputs are time-stamped textual files in folder tmp. The time format is YYYYMMDD-HHMMSS. In this case, every run will create a unique output file.

Run
-----------------------------
#. cd wan_test/wan_test
#. python wan_test_main.py

Run Tests
-------------------------
1. python setup.py test -s tests
2. Another way to run all the tests: Add key-value pair test_suite="tests" in setup.py (already added), and then run 'python setup.py test'.
3. Run a specified test suite : python setup.py test -s tests.test_access_url

Help About setup.py 
-------------------------
1. python setup.py --help

`Learn more <http://www.kennethreitz.org/essays/repository-structure-and-python>`_.

---------------

If you want to learn more about ``setup.py`` files, check out `this repository <https://github.com/kennethreitz/setup.py>`_.
