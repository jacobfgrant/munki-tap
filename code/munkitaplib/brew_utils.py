#!/usr/bin/python

#  Munkitap Brew Utils
#
#  brew_utils.py
#
#
#  Created by Jacob F. Grant
#
#  Written: 06/24/18
#  Updated: 06/27/18
#

"""
brew_utils.py

Functions for working with Homebrew.
"""

import json
import os
import subprocess

from munkitap_preferences import get_brew


# Homebrew Functions

def brew_installed():
    """Return if brew installed"""
    if not get_brew():
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


def install_latest_brew_formula(formula):
    """Install or upgrade a brew formula"""
    if True:
        brew_command = 'install'
    else:
        brew_command = 'upgrade'
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
    brew_installed()
 