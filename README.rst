WAN Test Suite
====================

A WAN test suite which simplifies the boring WAN test work easy and automatic.

Features Implemented
-----------------------------
ping, nslookup, portal retrieval, mail sending without proxy support at present.

Features to Be Implemented
-----------------------------
Formatted output, e.g., CSV format, Excel format, schedule tasks, and more.

Configuration File
-----------------------------
wan_test.ini, which holds all the input info. 

Ouput
-----------------------------
All the outputs are time-stamped textual files in folder tmp. The time format is YYYYMMDD-HHMMSS. In this case, every run will create a unique output file.

Run
-----------------------------
From your terminal (Windows CMD/Linux shell):
cd wan_test/wan_test
python wan_test_main.py
