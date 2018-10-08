#!/usr/bin/python

"""
Munkitap Brew Utils

brew_utils.py

Functions for working with Homebrew.


Created by Jacob F. Grant

Written: 06/24/18
Updated: 10/07/18
"""

import json
import os
import subprocess

from munkitap_preferences import get_brew
from utils import *


# Homebrew Functions

def brew_installed(quiet=False):
    """Return if brew installed"""
    if not get_brew():
        if not quiet:
            print "ERROR: brew not found. Please install Homebrew."
        return False
    else:
        return True


def is_brew_formula(formula, formula_list=None, quiet=False):
    """Check if formula in homebrew"""
    if not formula_list:
        formula_list = subprocess.check_output([get_brew(), 'search'])
        formula_list = formula_list.split('\n')[:-1]
    if formula in formula_list:
        if not quiet:
            print formula + " in homebrew"
        return True
    else:
        if not quiet:
            print formula + " not in homebrew"
        return False


def update_brew():
    """Update brew"""
    out, err = subprocess.Popen(
        [
            get_brew(),
            'update',
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    ).communicate()
    return out, err


def install_brew_tap(tap):
    """Installs a homebrew tap"""
    out, err = subprocess.Popen(
        [
            get_brew(),
            'tap',
            tap,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    ).communicate()
    return out, err


def install_latest_brew_formula(formula, quiet=False):
    """Install or upgrade a brew formula"""
    # Check formula info for install/up-to-date status
    out, err = subprocess.Popen(
        [
            get_brew(),
            'info',
            '--json=v1',
            formula
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    ).communicate()
    # Format JSON output and test for errors
    try:
        output = json.loads(out)[0]
    except TypeError:
        print "Error: " + formula + " not found"
        return out, err
    # Install if no versions installed
    if not output['installed']:
        brew_command = 'install'
        if not quiet:
            print "Installing " + formula
    # Upgrade if outdated
    elif output['outdated']:
        brew_command = 'upgrade'
        if not quiet:
            print "Upgrading " + formula
    # Return if installed and up-to-date
    else:
        print formula + " already installed and up-to-date"
        return out, err
    # Brew install/upgrade
    out, err = subprocess.Popen(
        [
            get_brew(),
            brew_command,
            formula,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    ).communicate()
    return out, err


def uninstall_brew_formula(formula):
    """Uninstall a brew formula"""
    out, err = subprocess.Popen(
        [
            get_brew(),
            'uninstall',
            formula,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    ).communicate()
    return out, err


if __name__ == "__main__":
    pass
 