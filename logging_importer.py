import importlib
from importlib.abc import Finder
import sys
import logging


class LoggingImporter(Finder):
    def find_module(self, name, path=None):
        if path:
            msg = "importing {} on {} by LoggingImporter".format(name, path)
        else:
            msg = "importing {} by LoggingImporter".format(name)
        # logging.info(msg)
        print(msg)
        # return None

sys.meta_path.insert(0, LoggingImporter())
