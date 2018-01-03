import logging
import os
from logging.handlers import RotatingFileHandler


class LogMessage:
    """
    :params - script_name/module_name, loglevel
        - initialise params defined under class
        - call log_creation module with params[module_name + '.log', loglevel, module_name]

    Task log_creation module will perform-
    1. find the Project absolute path using os module of python
    2. find the base_dir path where log directory exist
    3. check if log dir is not present then create it
    4. define formatter using logging module
    5. get log messages using getLogger function
    6. create logfile under log directory
    7. append the log data into newly created logfile
    8. add formatter to logfile
    9. set log level
    10. finally addHandler to logfile
    """

    def __init__(self, module_name, loglevel=logging.INFO):

        self.log = logging.getLogger(module_name)
        self.LogCreation(module_name+".log", loglevel, module_name)


    def LogCreation(self, logfilename, level, logger):

        PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

        BASE_DIR = os.path.dirname(PROJECT_PATH)

        if not os.path.exists(BASE_DIR):
            os.makedirs(BASE_DIR)

        log = logging.getLogger(logger)

        log_location = BASE_DIR+"/LogsDir/"+logfilename

        import pdb; pdb.set_trace()

        formatter = logging.Formatter('%(asctime)s %(levelname)s - %(message)s\r\n')
        file_handler = logging.FileHandler(filename=log_location, mode='a', encoding='utf-8')
        file_handler.setFormatter(formatter)

        if logfilename=="Sshdump":
            fh = RotatingFileHandler(filename=logfilename, mode='a', maxBytes=655351, backupCount=50, encoding="UTF-8")
            log.addHandler(fh)
        # fileRotation = RotatingFileHandler(filename=log_location, mode='a', encoding='utf-8', maxBytes=655351, backupCount=10)
        # fileRotation.setFormatter(formatter)


        log.setLevel(level)
        log.addHandler(file_handler)
        # log.addHandler(fileRotation)


def apploggerValidation():
    return True

if __name__ == '__main__':
    log_capta = LogMessage('test',)
    log_capta.log.info('This is informational message.')