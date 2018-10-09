#!/usr/bin/python

"""
Munkitap Utils

utils.py

Basic functions and utilities for Munkitap.


Created by Jacob F. Grant

Written: 07/02/18
Updated: 10/07/18
"""

from datetime import datetime
import os


# Functions

def create_dir(path):
    """Create a directory with error handling"""
    try: 
        os.makedirs(path)
    except OSError:
        if not os.path.isdir(path):
            raise


# Classes

class MunkitapLog(object):
    
    def __init__(self, quiet, verbose, logfile=None):
        self.quiet = quiet
        self.verbose = verbose
        self.logfile = logfile
        self._log_message("\nBeginning munkitap run at " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


    def _log_message(self, message):
        if self.logfile:
            with open(self.logfile, 'a+') as logfile:
                logfile.write("%s\n" % message)


    def print_message(self, message, verbose_message=None):
        if self.verbose and verbose_message:
            self._log_message(verbose_message)
            print verbose_message
        else:
            self._log_message(message)
            if not self.quiet:
                print message

    
    def log_to_file(self):
        self._log_message("Concluding munkitap run at " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == "__main__":
    pass
