import json
import logging
from AppLogger import LogMessage


log_capture = LogMessage("ReadJsonFile", loglevel=logging.DEBUG)
def ReadJsonFile():

    with open('/home/vignesh/Automation_Openstack/ConfigDir/AppData.json', 'r') as jsonFile:
        data = json.loads(jsonFile.read())
    log_capture.log.debug('json file has been loaded successfully!!!')

    return data

def jsonValidation():
    return True


if __name__ == '__main__':
    ReadJsonFile()
