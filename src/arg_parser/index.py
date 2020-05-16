#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Arg Parser
Handles command line arguments
"""

import argparse
from .args import *
from ..assets.methods import terminate
from ..assets.constants import PACK, UNPACK, CREATE

parser = argparse.ArgumentParser(
    description='Pack or unpack a given app directory')
method_parser = parser.add_subparsers(dest='method')


def init_args():
    """Instantiate the arguments for the main script

    Returns:
        args -- dict
            The arguments passed to the script
    """
    _generate_args()
    args, unknown = parser.parse_known_args()
    args = vars(args)
    _attempt_args_completion(args, unknown)
    _validate_args(args)
    return args


def _generate_args():
    """Generates each subparser's args with its given configuration
    """

    # ex. py4web-component.py pack foo -d apps/myapp -o foo.zip
    parser_pack = method_parser.add_parser(PACK)
    comp_arg(parser_pack)
    work_dir_arg(parser_pack)
    zip_arg(parser_pack)
    override_arg(parser_pack)

    # ex. py4web-component.py unpack -d apps/myapp -f foo.zip
    parser_unpack = method_parser.add_parser(UNPACK)
    work_dir_arg(parser_unpack)
    zip_arg(parser_unpack)
    force_arg(parser_unpack)

    # ex. py4web-component.py create foo apps/myapp
    parser_create = method_parser.add_parser(CREATE)
    comp_arg(parser_create)
    work_dir_arg(parser_create)
    force_arg(parser_create)


def _attempt_args_completion(args, unknown):
    """Attempts to fill in missing known args by using an array of unknown args passed

    Arguments:
        args {dict} -- known arguments
        unknown {list} -- unknown arguments
    """
    for key in args:
        if args[key] is None and len(unknown):
            args[key] = unknown.pop(0)


def _validate_args(args):
    """Validates the given script arguments

    Arguments:
        args {dict} -- The arguments passed to the script
    """

    for key in args:
        if args[key] is None:
            terminate("argument '{}' is required, got None".format(key))
