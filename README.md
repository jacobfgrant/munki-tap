# Munki-Tap

Munkitap is a tool for automatically building updated, stand-alone pkg installers from formulae in [Homebrew](https://github.com/Homebrew/brew) using Timothy Sutton's [brew-pkg](https://github.com/timsutton/brew-pkg) tool.

Eventually it should allow administrators to automatically upload these packages into munki; this functionality will be added in a future release.


## Installation

The easiest way to install munkitap is to use the .pkg installers under [Releases](https://github.com/jacobfgrant/munki-tap/releases). You can also using git to clone this repository and either run munkitap directly or use the provided script to build your own pkg.


## Usage

To use munkitap, use the `add` or `remove` commands to add/remove Homebrew formulae from the list of formulae "on tap." You can build the latest versions of these packages using the `munkitap pour` command.

More information can be found by running `munkitap --help`.
