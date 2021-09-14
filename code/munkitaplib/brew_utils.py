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


def brew_installed(log):
    """Return if brew installed"""
    if not get_brew():
        log.print_message("ERROR: brew not found. Please install Homebrew.")
        return False
    else:
        return True


def is_brew_formula(log, formula, formula_list=None):
    """Check if formula in homebrew"""
    if not formula_list:
        formula_list = subprocess.check_output([get_brew(), 'search', formula])

        formula_list = formula_list.split('\n')[:-1]

        # Use below to return if its a Cask or not, to avoid try/excepts
        # ar = '==> '
        # idxs = filter(lambda x: x > -1, [i for i, v in enumerate(formula_list) if ar in v])
        # formulae_idx = idxs[0]
        # cask_idx = idxs[1] if len(idxs) > 1 else len(formula_list) - 1

        # formulae = formula_list[1:cask_idx]
        # casks = formula_list[cask_idx + 1 :]

    if formula in formula_list:
        log.print_message(formula + " in homebrew")
        return True
    else:
        log.print_message(formula + " not in homebrew")
        return False


def get_brew_formula(log, formula):
    formula_info = {}
    brew_info = subprocess.check_output([get_brew(), 'info', '--json=v2', formula])
    brew_info = json.loads(brew_info)

    if len(brew_info.get('formulae', [])) > 0:
        formula_info = brew_info.get('formulae')[0]
    elif len(brew_info.get('casks', [])) > 0:
        formula_info = brew_info.get('casks')[0]

    return formula_info


def update_brew():
    """Update brew"""
    out, err = subprocess.Popen(
        [get_brew(), 'update'], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    ).communicate()
    return out, err


def install_brew_tap(tap):
    """Installs a homebrew tap"""
    out, err = subprocess.Popen(
        [get_brew(), 'tap', tap], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    ).communicate()
    return out, err


def install_latest_brew_formula(log, formula):
    """Install or upgrade a brew formula"""
    # Check formula info for install/up-to-date status
    out, err = subprocess.Popen(
        [get_brew(), 'info', '--json=v2', formula],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).communicate()
    # Format JSON output and test for errors
    try:
        brew_info = json.loads(out)

        if len(brew_info.get('formulae', [])) > 0:
            output = brew_info.get('formulae', [])[0]
        elif len(brew_info.get('casks', [])) > 0:
            output = brew_info.get('casks', [])[0]

    except TypeError:
        log.print_message("Error: " + formula + " not found")
        return out, err
    # Install if no versions installed
    if not output['installed']:
        brew_command = 'install'
        log.print_message("Installing " + formula)
    # Upgrade if outdated
    elif output['outdated']:
        brew_command = 'upgrade'
        log.print_message("Upgrading " + formula)
    # Return if installed and up-to-date
    else:
        log.print_message(formula + " already installed and up-to-date")
        return out, err
    # Brew install/upgrade
    out, err = subprocess.Popen(
        [get_brew(), brew_command, formula],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).communicate()
    return out, err


def uninstall_brew_formula(log, formula):
    """Uninstall a brew formula"""
    log.print_message("Uninstalling " + formula)
    out, err = subprocess.Popen(
        [get_brew(), 'uninstall', formula],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).communicate()
    return out, err


if __name__ == "__main__":
    pass
