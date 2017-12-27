import sys
import pip
import time


def package_installation_check():

    try:
        import time
        return True

    except:
        return False


def package_install(package='os', check=False):

    if check:
        print("{} Package is already installed!".format(package))

    else:

        pip.main(["install", package])
        time.sleep(2)
        sys.exit()


def package_uninstall(package):
    if package_installation_check():
        #for debugging: pip.main(["uninstall", package, "-vv"])
        pip.main(["uninstall", package])
        time.sleep(2)
        sys.exit()
    else:
        pass


if __name__ == '__main__':


    if package_installation_check():
        package_install(package='time', check=True)


    # package_install("fabric")
    # package_install("select")

    # package_install("logging")
    # package_install("os")
    # package_install("sys")
    # package_install("json")
    # package_install("exception")
    # package_install("re")




#pip install -e git+https://github.com/paramiko/paramiko/#egg=paramiko