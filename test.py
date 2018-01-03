import os

files = []
path_name = os.path.join(os.path.dirname(os.path.abspath(os.getcwd())), '.ssh/')
print(path_name)


for root, directories, filenames in os.walk(path_name):
    if not filenames:
        os.system('test -f ~/.ssh/id_rsa.pub || ssh-keygen -t rsa -N "" -f ~/.ssh/id_rsa')

else:
    pass



