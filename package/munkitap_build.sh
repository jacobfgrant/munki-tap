#!/bin/bash

#  Munkitap Pkg Build Script
#
#  munkitap_build.sh
#
#
#  Created by Jacob F. Grant
#
#  Written: 06/28/18
#  Updated: 10/07/18
#


# Check for requirements
MUNKIPKG=$(which munkipkg)

if [ ! -e "$MUNKIPKG" ]
then
    echo 'munkipkg not found'
    exit 1
fi

if [ ! -f "build-info.plist" ]
then
    echo 'build-info.plist not found'
    exit 2
fi

if [ ! -f "../code/munkitap" ] || [ ! -d "../code/munkitaplib" ]
then
    echo 'munkitap files not found'
    exit 3
fi

# Create payload directory
if [ -d "./payload" ]
then
    rm -r ./payload
fi
mkdir -p ./payload/Library/Munkitap/
mkdir -p ./payload/Library/LaunchAgents/
mkdir -p ./payload/usr/local/bin/

# Copy munkitap files
cp ../code/munkitap ./payload/Library/Munkitap/
cp -r ../code/munkitaplib ./payload/Library/Munkitap/
cp ./launchd/com.github.munkitap.plist ./payload/Library/LaunchAgents/

# Create symbolic link in /usr/local/bin/
ln -s /Library/Munkitap/munkitap ./payload/usr/local/bin/munkitap

# Build package
"$MUNKIPKG" .
