#!/usr/bin/python

#  Munkitap Preferences
#
#  munkitap_preferences.py
#
#
#  Created by Jacob F. Grant
#
#  Written: 06/24/18
#  Updated: 07/03/18
#

"""
munkitap_preferences.py

Functions for getting and setting Munkitap preferences.
"""

import os
import subprocess

# Disable Pylint warnings
# pylint: disable=E0611
from CoreFoundation import CFPreferencesAppSynchronize, \
                            CFPreferencesCopyAppValue, \
                            CFPreferencesSetAppValue
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
            raise PreferenceError(
                "Could not synchronize %s preference: %s" % key)
    except Exception, err:
        raise PreferenceError(
            "Could not set %s preference: %s" % (key, err))


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
            print "ERROR: brew not found.\nPlease install Homebrew."
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
        formula_info = {}
        set_pref('FORMULA_INFO', formula_info)
    return formula_info


def get_git():
    """Get the system git path"""
    git_path = get_pref('GIT_PATH')
    if not git_path or not os.path.isfile(git_path):
        try:
            git_path = subprocess.check_output(['which', 'git']).split('\n')[0]
            set_pref('GIT_PATH', git_path)
        except subprocess.CalledProcessError:
            print "ERROR: git not found.\nPlease install Git."
    return git_path


def get_id():
    """Get package identifier"""
    identifier = get_pref('IDENTIFIER')
    if not identifier:
        identifier = 'com.munkitap'
        set_pref('IDENTIFIER', identifier)
    return identifier


def get_munki_repo():
    """Get Munki repo path"""
    return '/Volumes/munki-repo/'


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


# Testing Preferences

def initialize_preferences():
    """Create preferences"""
    # Brew
    print get_brew()
    # Cache
    print get_cache()
    # Formula Info
    print get_formula_info()
    # Git
    print get_git()
    # Munki
    get_munki_repo()
    # On Tap
    print get_on_tap()


if __name__ == "__main__":
    initialize_preferences()
