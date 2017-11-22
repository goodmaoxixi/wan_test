# wan_test
A WAN test suite.

# Features Implemented
ping, nslookup, portal retrieval, mail sending without proxy support at present.

# Features to Be Implemented
Formatted output, e.g., CSV format, Excel format, schedule tasks, and more.

# Configuration File
wan_test.ini, which holds all the input info. 

# Ouput
All the outputs are time-stamped textual files in folder tmp. The time format is YYYYMMDD-HHMMSS. In this case, every run will create a unique output file.

# Run
python wan_test_main.py
