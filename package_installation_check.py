import sys
import pip
import time


def package_installation_check(package):

    try:
        import package
        return True

    except:
        return False

def package_install(package):

    if package_installation_check(package):
        print("{} Package is already installed!".format(package))

    else:

        pip.main(["install", package])
        time.sleep(2)
        sys.exit()


def package_uninstall(package):
    if package_installation_check(package):
        #for debugging: pip.main(["uninstall", package, "-vv"])
        pip.main(["uninstall", package])
        time.sleep(2)
        sys.exit()
    else:
        pass

if __name__ == '__main__':
    pass

#pip install -e git+https://github.com/paramiko/paramiko/#egg=paramiko