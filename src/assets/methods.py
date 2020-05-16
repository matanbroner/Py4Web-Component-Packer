#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Methods
A series of helper methods to assist the module
"""

import sys
import os
import shutil
import zipfile


def local_dir():
    """ Returns the working directory for the main script

    Returns:
        str -- working directory
    """
    return os.getcwd()


def script_name():
    """ The name of the main script

    Returns:
        str -- script name (ex. foo.py)
    """
    return sys.argv[0]


def base_file_name(file_name):
    """ Returns the base name of a file, with no extension

    Arguments:
        file_name {str} -- complete filename

    Returns:
        str -- base file name (ex. foo.py -> foo)
    """
    return os.path.splitext(file_name)[0]


def join_paths(paths):
    """ Joins a list of strings as a file path

    Arguments:
        paths {list} -- source elements (ex. ['foo', 'bar'])

    Returns:
        [type] -- [description]
    """
    return '/'.join(paths)


def path_exists(path):
    """ Determines if a file path can be read

    Arguments:
        path {str} -- file path

    Returns:
        [type] -- [description]
    """
    return os.path.exists(path)


def delete_directory(path):
    """ Deletes a directory

    Arguments:
        path {str} -- directory path
    """
    shutil.rmtree(path)


def copy_file(src, dest):
    """ Copies a file to a given source directory, creating necessary tree

    Arguments:
        src {str} -- source path
        dest {str} -- destination path
    """
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    shutil.copyfile(src, dest)


def zip_dir(src, name, ext='zip'):
    """ Zips a directory to a given name

    Arguments:
        src {str} -- source directory
        name {str} -- name of the archive created

    Keyword Arguments:
        ext {str} -- optional extension (default: {'zip'})
    """
    shutil.make_archive(name, ext, src)


def unzip_dir(src, dest, folder='', ext='zip'):
    if len(folder):
        dest = join_paths([dest, folder])
    shutil.unpack_archive(src, dest, ext)


def terminate(message):
    """ Terminates the script

    Arguments:
        message {str} -- message to exit with
    """
    sys.exit("{0}: error: {1}".format(script_name(), message))
