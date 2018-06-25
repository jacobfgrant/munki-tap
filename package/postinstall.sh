#!/bin/bash

#  Munkitap Postinstall Script
#
#  postinstall.sh
#
#
#  Created by Jacob F. Grant
#
#  Written: 06/24/18
#  Updated: 06/25/18
#

# Link munkitap in PATH
if ! [ -L "$3"usr/local/bin/munkitap ]
then
    ln -s "$3"Library/Munkitap/munkitap "$3"usr/local/bin/munkitap
fi
