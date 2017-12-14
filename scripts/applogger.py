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

class logMessage:

    def __init__(self, module_name, loglevel=logging.INFO):
        self.log_creation(module_name + '.log', loglevel, module_name)
        self.log = logging.getLogger(module_name)

    def log_creation(self, logfilename, level, logger):

        PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
        BASE_DIR = os.path.dirname(PROJECT_PATH)

        if not os.path.exists(BASE_DIR):
            os.makedirs(BASE_DIR)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
