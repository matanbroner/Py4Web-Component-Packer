#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Args
A series of command line arguments that accept a given parser
"""

import os
from ..assets.methods import local_dir


def comp_arg(parser):
    """ Component name
    """
    parser.add_argument('component',
                        nargs='?',
                        help='component directory name')


def work_dir_arg(parser):
    """ Working directory to either pack to or unpack from
    """
    parser.add_argument('-d',
                        nargs='?',
                        dest='work_dir',
                        default=local_dir(),
                        help='working apps directory')


def zip_arg(parser):
    """ Zip file to either create or decompress
    """
    parser.add_argument('zip',
                        nargs='?',
                        help='zip file name')


def force_arg(parser):
    """ Force write over in unpack
    """
    parser.add_argument('-f',
                        dest='force',
                        action='store_true',
                        help='write over the exiting destination directory')


def override_arg(parser):
    """ Force file override in pack
    """
    parser.add_argument('-o',
                        dest='override',
                        action='store_true',
                        help='override the current destination zip')
