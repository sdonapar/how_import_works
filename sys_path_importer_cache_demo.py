import sys
import os
import importlib
from importlib.util import find_spec
from importlib import find_loader


def print_sys_path_importer_cache():
    for key in sys.path_importer_cache:
        if not 'python3.6' in key:
            print(key)

find_loader('spam')

curdir = os.path.abspath(os.curdir)
module2_dir = os.path.join(curdir, 'module2')
print("Adding " + curdir + " to sys.path")
sys.path.append(curdir)
print("Finding spam module:")
find_loader('spam')
print("Adding " + module2_dir + " to sys.path")
sys.path.append(module2_dir)

print_sys_path_importer_cache()

loader = find_loader('spam')
loader.load_module('spam')

print_sys_path_importer_cache()

pkg_spec = find_spec('pkg.foo.relative')
relative = pkg_spec.loader.load_module('pkg.foo.relative')

print_sys_path_importer_cache()
