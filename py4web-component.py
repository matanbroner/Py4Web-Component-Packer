#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Py4Web Component
A configurable command line tool that makes component packing and unpacking easy
"""

from lib.arg_parser.index import init_args
from lib.directory_handler.index import DirectoryHandler


def main():
    args = init_args()
    DirectoryHandler(args).activate()


main()
