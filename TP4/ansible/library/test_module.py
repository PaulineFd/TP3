#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

import shutil

shutil.copytree ("/usr, ~/archives")
