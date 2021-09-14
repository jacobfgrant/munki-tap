#!/usr/bin/python

"""
Munkitap Preferences

munkitap_preferences.py

Functions for getting and setting Munkitap preferences.


Created by Jacob F. Grant

Written: 06/24/18
Updated: 10/07/18
"""

import os
import subprocess

# Disable Pylint warnings
# pylint: disable=E0611
from CoreFoundation import (
    CFPreferencesAppSynchronize,
    CFPreferencesCopyAppValue,
    CFPreferencesSetAppValue,
)

# pylint: enable=E0611

from utils import *


BUNDLE_ID = 'com.github.munkitap'


### Exceptions


class PreferenceError(Exception):
    """Preference exception"""

    pass


### Low-level prefs API


def get_pref(key, domain=BUNDLE_ID):
    """Get preference value"""
    return CFPreferencesCopyAppValue(key, domain)


def set_pref(key, value, domain=BUNDLE_ID):
    """Set preference value"""
    try:
        CFPreferencesSetAppValue(key, value, domain)
        if not CFPreferencesAppSynchronize(domain):
            raise PreferenceError("Could not synchronize %s preference: %s" % key)
    except Exception, err:
        raise PreferenceError("Could not set %s preference: %s" % (key, err))


### High-level prefs APIs

# Get functions


def get_brew():
    """Get brew path"""
    brew_path = get_pref('BREW_PATH')
    if not brew_path or not os.path.isfile(brew_path):
        try:
            brew_path = subprocess.check_output(['which', 'brew']).split('\n')[0]
            set_pref('BREW_PATH', brew_path)
        except subprocess.CalledProcessError:
            pass
    return brew_path


def get_cache():
    """Get munkitap cache"""
    cache = get_pref('CACHE')
    if not cache:
        cache = os.path.join(os.getenv("HOME"), 'Library/Munkitap/')
        set_pref('CACHE', cache)
    create_dir(cache)
    return cache


def get_formula_info():
    """Get formula info"""
    formula_info = get_pref('FORMULA_INFO')
    if not formula_info:
        brew_info = subprocess.check_output([get_brew(), 'info', '--json=v2', formula])
        brew_info = json.loads(brew_info)

        if len(brew_info.get('formulae', [])) > 0:
            formula_info = brew_info.get('formulae', [])[0]
        elif len(brew_info.get('casks', [])) > 0:
            formula_info = brew_info.get('casks', [])[0]

        set_pref('FORMULA_INFO', formula_info)
    return formula_info


def get_id():
    """Get package identifier"""
    identifier = get_pref('IDENTIFIER')
    if not identifier:
        identifier = 'com.munkitap'
        set_pref('IDENTIFIER', identifier)
    return identifier


def get_munki_catalog():
    """Get Munki catalog"""
    munki_catalog = get_pref('MUNKI_CATALOG')
    if not munki_catalog:
        munki_catalog = 'testing'
        set_pref('MUNKI_CATALOG', munki_catalog)
    return munki_catalog


def get_munki_repo():
    """Get Munki repo path"""
    munki_repo = get_pref('MUNKI_REPO')
    if not munki_repo:
        munki_repo = ''
        set_pref('MUNKI_REPO', munki_repo)
    return munki_repo


def get_munki_subdir():
    """Get Munki subdirectory for munkitap"""
    munki_subdir = get_pref('MUNKI_SUBDIR')
    if not munki_subdir:
        munki_subdir = 'munkitap'
        set_pref('MUNKI_SUBDIR', munki_subdir)
    return munki_subdir


def get_on_tap():
    """Get formulas 'on tap'"""
    on_tap = get_pref('ON_TAP')
    if not on_tap:
        on_tap = []
        set_pref('ON_TAP', on_tap)
    return on_tap


# Set functions


def set_cache(cache):
    """Set cache location"""
    cache = os.path.expanduser(cache)
    if os.path.isfile(cache):
        print "ERROR: " + cache + " already exists as a file"
        return
    set_pref('CACHE', cache)


def set_id(identifier):
    """Set identifier"""
    set_pref('IDENTIFIER', identifier)


def set_munki_catalog(munki_catalog):
    """Set Munki catalog"""
    set_pref('MUNKI_CATALOG', munki_catalog)


def set_munki_repo(munki_repo):
    """Set Munki repo path"""
    set_pref('MUNKI_REPO', munki_repo)


def set_munki_subdir(munki_subdir):
    """Set Munki subdirectory for munkitap"""
    set_pref('MUNKI_SUBDIR', munki_subdir)


# Testing Preferences


def initialize_preferences():
    """Create preferences"""
    # Brew
    print get_brew()
    # Cache
    print get_cache()
    # Formula Info
    print get_formula_info()
    # Munki
    get_munki_repo()
    # On Tap
    print get_on_tap()


if __name__ == "__main__":
    initialize_preferences()
