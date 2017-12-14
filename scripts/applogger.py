import logging
import os

"""
:params - script_name/module_name, loglevel
    - initialise params defined under class
    - call log_creation module with params[module_name + '.log', loglevel, module_name]
    
Task log_creation module will perform-
1. find the Project absolute path using os module of python
2. find the base_dir path where log directory exist
3. check if log dir is not present then create it
4. define formatter using logging module
5. create logfile under log directory
6. append the log data into newly created logfile
7. add formatter to logfile
8. set log level
9. finally addHandler to logfile
"""

