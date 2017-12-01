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
