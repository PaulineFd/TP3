#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import os
import zipfile

def zipdir(/files/TP4, ziph)
    for root, dirs, files in os.walk(/files/TP4):
            for file in files:
                ziph.write(os.path.join(root,file))
zipf= zipfile.Zipfile('Zipped_file.zip','w', zipfile.ZIP_DEFLATED)
zipdir('backup', zipf)
zipf.close()

# def main():
#     module = AnsibleModule(

#     )
# if __name__ == '__main__':
#     main()

