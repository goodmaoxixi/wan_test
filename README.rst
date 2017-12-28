WAN Test Suite
====================

A WAN test suite which simplifies the boring WAN test work with automatic schedule tasks.

Features Implemented
-----------------------------
1. ping
2. nslookup
3. Portal retrieval
4. Mail sending via SMTP 25 without proxy and SSL support

Features to Be Implemented
-----------------------------
1. Sending an email behind proxy using SSL
2. Formatted output, e.g., CSV format, Excel format
3. schedule tasks, and more

Configuration File
-----------------------------
Create a folder named wantest/tmp under the root foler of this suite. Use wantest/wantest.ini as a template and copy it to folder wantest/tmp and customize it as you wish. If you do not do this in advance, the suite will do it for you automatically. So please keep in mind that wantest/tmp/wantest.ini is the the actual configuration file that the suite reads.

Ouput
-----------------------------
All the outputs are time-stamped textual files in folder tmp. The time format is YYYYMMDD-HHMMSS. In this case, every run will create a unique output file.

Run
-----------------------------
From your DOS prompt and terminal, python wantest/wantest_main.py, or use any relative or absolute path to start it. Create a shortcut if you like to.

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
