#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Directory Handler
Overarching handler for the module, parses command line args and enacts correct method
"""


from ..assets.methods import base_file_name, join_paths, path_exists, terminate
from ..assets.constants import PACK, UNPACK
from ..config import files, replace_char
from .pack import Pack
from .unpack import Unpack


class DirectoryHandler:
    def __init__(self, config):
        self.config = config
        self._configure(config)

    def activate(self):
        """ Activates a given DirectoryHandler instance
        """
        self.handlers[self.method]()

    def _configure(self, config):
        """ Configuration function for DirectoryHandler

        Arguments:
            config {dict} -- configuration keys (includes command line args)
        """
        self.handlers = {
            PACK: self._pack,
            UNPACK: self._unpack
        }
        for key in config:
            setattr(self, key, config[key])
        self.base_file = base_file_name(self.zip)
        self._generate_read_files()
        self._generate_file_paths()

    def _pack(self):
        """ Pack functionality activator
        """
        self._validate_file_paths()
        config = self.config.copy()
        config['file_names'] = self.file_names
        Pack(config).activate(self.file_paths)

    def _unpack(self):
        """ Unpack functionality wrapper
        """
        config = self.config.copy()
        config['file_names'] = self.file_names
        Unpack(config).activate(self.file_paths)

    def _generate_read_files(self):
        """ Generates a series of file names according to config and component name
        """
        file_names = []
        use_file = self._use_file_name()
        for file_name in files:
            file_names.append(file_name.replace(replace_char, use_file))
        self.file_names = file_names

    def _generate_file_paths(self):
        """ Generates necessary file paths associated with component name
        """
        use_file = self._use_file_name()
        file_paths = []
        for name in self.file_names:
            file_paths.append(join_paths(
                [self.work_dir, use_file, name]))
        self.file_paths = file_paths

    def _validate_file_paths(self):
        """ Ensures a Pack's file_paths are all readable
        """
        for path in self.file_paths:
            if not path_exists(path):
                terminate(
                    "expected file at {} but could not find or read".format(path))

    def _use_file_name(self):
        """Detemines whether to use base zip file name or component name based on method

        Returns:
            str -- file name
        """
        return self.component if self.method == PACK else self.base_file
