#!/usr/bin/python

"""
Munkitap Utils

utils.py

Basic functions and utilities for Munkitap.


Created by Jacob F. Grant

Written: 07/02/18
Updated: 10/07/18
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
