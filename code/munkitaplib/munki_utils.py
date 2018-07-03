#!/usr/bin/python

#  Munkitap Munki Utils
#
#  munki_utils.py
#
#
#  Created by Jacob F. Grant
#
#  Written: 06/29/18
#  Updated: 07/03/18
#

"""
munki_utils.py

Functions for importing packages into Munki.
"""

import os
import shutil
import subprocess

from FoundationPlist import *

from utils import *


# Functions

def munkitools_installed():
    """Return if required munki installed"""
    if not os.path.isfile('/usr/local/munki/managedsoftwareupdate'):
        return False
    if not os.path.isfile('/usr/local/munki/makepkginfo'):
        return False
    if not os.path.isfile('/usr/local/munki/makecatalogs'):
        return False
    return True


def get_all_catalog_info(repo_path):
    """Return dictionary of all catalog info"""
    all_items_path = os.path.join(
        repo_path,
        'catalogs',
        'all'
    )
    if not os.path.exists(all_items_path):
        catalog_info = []
    else:
        catalog_info = readPlist(all_items_path)
    return catalog_info


def generate_already_in_munki(catalog_info):
    """Return lambda function for checking if pkginfo exists in munki"""
    item_hashes = []
    for item in catalog_info:
        try:
            item_hashes.append(item['installer_item_hash'])
        except KeyError:
            pass
    return lambda pkginfo : pkginfo['installer_item_hash'] in item_hashes


def get_pkginfo(pkg, name, desc, url, catalog, quiet=False):
    """Return packageinfo file for a pkg"""
    if not quiet:
        print "Generating pkginfo for " + pkg
    description = desc + '.\n\n' + url
    proc = subprocess.Popen(
        [
            '/usr/local/munki/makepkginfo',
            pkg,
            '--displayname',
            name,
            '--description',
            description,
            '--catalog',
            catalog,
            '--category',
            'Munkitap',
            '--developer',
            'Homebrew'
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    out, err = proc.communicate()
    if not err:
        return readPlistFromString(out)
    else:
        return None


def add_pkg_to_munki(pkg, pkginfo, repo_path, repo_subdirectory, quiet=False):
    """Adds a pkg to munki"""
    pkginfo_dest_path = os.path.join(repo_path, 'pkgsinfo', repo_subdirectory)
    pkg_dest_path = os.path.join(repo_path, 'pkgs', repo_subdirectory)
    create_dir(pkginfo_dest_path)
    create_dir(pkg_dest_path)
    name = "%s-%s" % (
        pkginfo["name"],
        pkginfo["version"].strip()
    )
    pkginfo_path = os.path.join(pkginfo_dest_path, name)
    pkg_path = os.path.join(pkg_dest_path, (name + '.pkg'))
    index = 0
    while os.path.exists(pkg_path) or os.path.exists(pkginfo_path):
        index += 1
        name = "%s-%s__%s" % (
            pkginfo['name'],
            pkginfo['version'],
            index
        )
        pkginfo_path = os.path.join(pkginfo_dest_path, name)
        pkg_path = os.path.join(pkg_dest_path, (name + '.pkg'))
    if not quiet:
        print "Copying pkginfo for " + name + " to " + pkginfo_path
        print "Copying " + name + ".pkg to " + pkg_path
    # Set installer_item_location
    pkginfo = dict(pkginfo)
    pkginfo['installer_item_location'] = os.path.join(repo_subdirectory, (name + '.pkg'))
    writePlist(pkginfo, pkginfo_path)
    shutil.copyfile(pkg, pkg_path)
    return pkginfo_path, pkg_path


def run_makecatalogs(repo_path, quiet=False):
    """Run munki makecatalogs"""
    if not quiet:
        print "Running makecatalogs"
    out, err = subprocess.Popen(
        [
            '/usr/local/munki/makecatalogs',
            repo_path
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    ).communicate()
    return out, err


if __name__ == "__main__":
    pass
