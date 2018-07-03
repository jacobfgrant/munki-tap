#!/usr/bin/python

#  Munkitap Utils
#
#  utils.py
#
#
#  Created by Jacob F. Grant
#
#  Written: 07/02/18
#  Updated: 07/03/18
#

"""
utils.py

Basic functions and utilities.
"""

import os


# Functions

def create_dir(path):
    """Create a directory with error handling"""
    try: 
        os.makedirs(path)
    except OSError:
        if not os.path.isdir(path):
            raise


if __name__ == "__main__":
    pass
