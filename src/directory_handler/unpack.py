#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Unpack
Handles decompression functionality
"""

from ..assets.methods import base_file_name, path_exists, unzip_dir, terminate


class Unpack:
    def __init__(self, config):
        self._configure(config)

    def activate(self, file_paths):
        """ Activates a given Pack instance, creates compression file
        """
        self._verify_file_existence(file_paths)
        self._unzip_files()

    def _configure(self, config):
        """ Configuration function for Pack

        Arguments:
            config {dict} -- configuration keys (includes command line args)
        """
        for key in config:
            setattr(self, key, config[key])

    def _verify_file_existence(self, file_paths):
        """Ensures that either the force flag exists or that files do not exist before decompression

        Arguments:
            file_paths {list} -- list of files to decompress
        """
        if self.force:
            return
        for path in file_paths:
            if path_exists(path):
                terminate(
                    "file {} exists, use -f to force write over existing copy".format(path))

    def _unzip_files(self):
        """ Decompresses the provided compression file
        """
        if not path_exists(self.zip):
            terminate(
                "zip file {} was not found or able to be read".format(self.zip))
        unzip_dir(self.zip, self.work_dir, folder=base_file_name(self.zip))
