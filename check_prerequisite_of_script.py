from imp import find_module
import sys
import pip
import time



def better_way_of_package_check(list_of_package):
    dict_container = {}
    for item in list_of_package:
        try:
            find_module(item)
            dict_container[item] = 'Y'
            print("{0:10} :--> Installed".format(item))
        except ImportError as err:
            dict_container[item] = 'N'
            print("{0:10} :--> Not Installed".format(item))
    # import pdb; pdb.set_trace()
    package_install(dict_container)


def package_install(dict_container):

    list_of_package = [k for k, v in dict_container.items() if v == 'N']
    # import pdb; pdb.set_trace()
    if not list_of_package:
        print("\n***All the Packages are installed***\n")
    else:
        for item in list_of_package:
            pip.main(["install", item])
            time.sleep(2)


def package_uninstall(package):
    #for debugging: pip.main(["uninstall", package, "-vv"])
    pip.main(["uninstall", package])
    time.sleep(2)
    sys.exit()



if __name__ == '__main__':

    list_of_package = [ "select", "logging", "os", "sys", "json", "exception", "re"]
    better_way_of_package_check(list_of_package)
    package_uninstall("fabric")


    # if d[list_of_package[0]] == "Installed":
    #     package_uninstall(list_of_package[0])


    # if package_installation_check():
    #     package_install(package='time', check=True)
    #

    # package_install("fabric")
    # package_install("select")

    # package_install("logging")
    # package_install("os")
    # package_install("sys")
    # package_install("json")
    # package_install("exception")
    # package_install("re")




#pip install -e git+https://github.com/paramiko/paramiko/#egg=paramiko