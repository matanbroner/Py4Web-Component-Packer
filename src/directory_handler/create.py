#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Create
Handles new component tree generation
"""

from ..assets.methods import path_exists, create_file, terminate


class Create:
    def __init__(self, config):
        self._configure(config)

    def activate(self, file_paths):
        """ Activates a given Create instance, creates compression file
        """
        self._create_tree(file_paths)

    def _configure(self, config):
        """ Configuration function for Create

        Arguments:
            config {dict} -- configuration keys (includes command line args)
        """
        for key in config:
            setattr(self, key, config[key])

    def _create_tree(self, file_paths):
        """Generates new component tree

        Arguments:
            file_paths {list} -- list of files to create
        """
        for path in file_paths:
            if path_exists(path) and not self.force:
                terminate(
                    "file {} exists, use -f to force write over existing copy".format(path))
            create_file(path)
