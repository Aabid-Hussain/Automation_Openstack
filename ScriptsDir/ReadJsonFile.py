import json
import logging
from AppLogger import logMessage


log_capture = logMessage("readJsonFile", loglevel=logging.DEBUG)
def readJsonFile():

    with open('/home/vignesh/Automation_Openstack/config/appdata.json', 'r') as jsonFile:
        data = json.loads(jsonFile.read())
    log_capture.log.debug('json file has been loaded successfully!!!')

    return data

def jsonValidation():
    return True


if __name__ == '__main__':
    readJsonFile()
