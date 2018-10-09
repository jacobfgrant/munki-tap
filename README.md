# Munki-Tap

Munkitap is a tool for automatically building updated, stand-alone pkg installers from formulae in [Homebrew](https://github.com/Homebrew/brew) using Timothy Sutton's [brew-pkg](https://github.com/timsutton/brew-pkg) tool.

It can also automatically add these packages to a mounted munki repo.


## Installation

The easiest way to install munkitap is to use the .pkg installers under [Releases](https://github.com/jacobfgrant/munki-tap/releases). You can also using git to clone this repository and either run munkitap directly or use the provided script to build your own pkg.


## Usage

To use munkitap, use the `add` or `remove` commands to add/remove Homebrew formulae from the list of formulae "on tap." You can build the latest versions of these packages using the `munkitap pour` command.

More information can be found by running `munkitap --help`.


### Munkitap
```
usage: munkitap [-h] [-q | -v] {add,remove,pour,set,list} ...

Automates building pkg files from brew formulae.

optional arguments:
  -h, --help            show this help message and exit
  -q, --quiet           Run munkitap silently. (Mutally exclusive with
                        --verbose.)
  -v, --verbose         Run munkitap with more verbose output. (Mutally
                        exclusive with --quiet.)

Munkitap commands:
  (command line options for munkitap)

  {add,remove,pour,set,list}
                        additional help
    add                 Add brew formula to munkitap
    remove              Remove brew formula from munkitap
    pour                Pour munkitap formulas (build packages)
    set                 Set munkitap preferences
    list                Show all formulae in munkitap
```
    
##### Munkitap Add
```
usage: munkitap add [-h] [-i] formula

positional arguments:
  formula        Brew formula to add to munkitap

optional arguments:
  -h, --help     show this help message and exit
  -i, --install  Tells brew to install/upgrade the given formula
```


##### Munkitap Remove

```
usage: munkitap remove [-h] [-u] formula

positional arguments:
  formula          Brew formula to remove from munkitap

optional arguments:
  -h, --help       show this help message and exit
  -u, --uninstall  Tells brew to uninstall the given formula
```


##### Munkitap Pour

```
usage: munkitap pour [-h] [-f] [-id] [-m]

optional arguments:
  -h, --help            show this help message and exit
  -f, --formula     Pour a specific formula
  -id, --identifier 
                        Use the specified identifer
  -m, --skip-munki      Skip importing packages into munki
```


##### Munkitap Set

```
usage: munkitap set [-h] [-c] [-id] [-mc] [-mr] [-ms]

optional arguments:
  -h, --help            show this help message and exit
  -c, --cache       Set the munkitap pkg cache location
  -id, --identifier 
                        Set the pkg identifier
  -mc, --munki-catalog 
                        Set the munki default catalog
  -mr, --munki-repo 
                        Set the munki repo path
  -ms, --munki-subdir 
                        Set the munki subdirectory for munkitap
```


##### Munkitap List

```
usage: munkitap list [-h] [-f] [-i]

optional arguments:
  -h, --help         show this help message and exit
  -f, --formula  Show a specific formula
  -i, --info         Show formula information
```
