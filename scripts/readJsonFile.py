import json


def readJsonFile():

    with open('/home/vignesh/Automation_Openstack/config/appdata.json', 'r') as jsonFile:
        data = json.loads(jsonFile.read())

    return data

def jsonValidation():
    return True


if __name__ == '__main__':
    readJsonFile()
