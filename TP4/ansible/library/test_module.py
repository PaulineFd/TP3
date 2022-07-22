#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import os
import zipfile

def retrieve_file_paths(dir_name):
    filePaths = []
    for root, directories, files in os.walk(dir_name):
        for filename in files:
            filePath = os.path.join(root, filename)
            filePaths.append(filePath)
    return filePaths 

def main():
    dir_name = 'TP4'
    filePaths = retrieve_file_paths(dir_name)
    print('The following list of files will be zipped: ')
    for fileName in filePaths:
        print(fileName)
    
    zip_file = zipfile.ZipFile(dir_name+'.zip', 'w')
    with zip_file:
        for file in filePaths:
            zip_file.write(file)
    print(dir_name+'.zip is created successfully!')
    
    module_args = dict(
        dir_name = dict(type = str, required = True),
        filePaths = dict(type = str,required = True)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
     )

    result = dict(
        changes=False
     )
    module.exit_json(**result)

if __name__ == "__main__" :
    main()

