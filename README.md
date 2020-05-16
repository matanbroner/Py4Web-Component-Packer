# Py4Web Component Packer

A configurable command line tool that makes component creation, packing, and unpacking easy

## Modes

**Pack**
Allows for the compressing of a series of components structure files into a dynamically named zip file.

**Unpack**
Decompresses a component structure into a working apps directory.

**Create**
Generates a new component file structure with all listed files in the configuration file

## Usage

**Arguments**

    # Positional
    method: usage mode, one of ['pack', 'unpack', 'create']
    component: directory name of component (only valid for pack)
    zip: compression file to compress or decompress

    # Flags
    -d: working apps directory
    -f: force rewrite of exisitng files (only valid for unpack)
    -o: override of existing zip file (only valid for pack)

The module makes a best effort to allow for any ordering of arguments passed in through redistributing unknown arguments into missing known arguments, but is suggested that positional arguments precede flag arguments.

**Example Usages**

    # Pack
    py4web-component.py pack foo -d apps/myapp -o foo.zip

    # Unpack
    py4web-component.py unpack -d apps/myapp -f foo.zip

    # Create
    py4web-component.py create foo -d apps/myapp -f

## Configuration

The files that are packed and unpacked by default are:

    *.py,
    static/components/*.html
    static/components/*.js
    static/components/*.css

Where each \* represents the component name which is injected dynamically. To modify the files that are modified, change these listed files in `/src/config.py` whilst following the same style of insertion.

## Help

You are able to learn about each argument by using either of the following:

    py4web-component.py pack -h
    py4web-component.py unpack -h
    py4web-component.py create -h

Which will lead to output similar to:

    usage: py4web-component.py unpack [-h] [-d [WORK_DIR]] [-f] [zip]
    positional arguments:
     zip            zip file name
    optional arguments:
    -h, --help     show this help message and exit
    -d [WORK_DIR]  working apps directory
    -f             write over the exiting destination directory

## Contributors

Matan Broner, UCSC 2020
