import importlib
from importlib.abc import Finder
import sys


class LoggingImporter(Finder):
    def find_module(self, name, path=None):
        if path:
            msg = "importing {} on {} by LoggingImporter".format(name, path)
        else:
            msg = "importing {} by LoggingImporter".format(name)
        print(msg)
        return None 
