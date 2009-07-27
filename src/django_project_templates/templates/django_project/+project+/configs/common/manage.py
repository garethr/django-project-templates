#!/usr/bin/env python

import os
import sys

# we want a few paths on the python path
# first up we add the root above the application so
# we can have absolute paths everywhere
python_path = os.path.join(
    os.path.realpath(os.path.dirname(__file__)), '../../../'
)
# we have have a local apps directory
apps_path = os.path.join(
    os.path.realpath(os.path.dirname(__file__)), '../../apps'
)
# we have have a local externals directory
# which saves you having to install a load of
# python modules locally and get into a versioning
# issue
ext_path = os.path.join(
    os.path.realpath(os.path.dirname(__file__)), '../../../ext'
)

# we add them first to avoid any collisions
sys.path.insert(0, python_path)
sys.path.insert(0, apps_path)
sys.path.insert(0, ext_path)

from django.core.management import execute_manager
try:
    import settings # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

if __name__ == "__main__":
    execute_manager(settings)
