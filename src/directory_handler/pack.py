#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Pack
Handles compression functionality
"""


from ..assets.methods import base_file_name, path_exists, join_paths, delete_directory, copy_file, zip_dir, terminate


class Pack:
    def __init__(self, config):
        self._configure(config)

    def activate(self, file_paths):
        """ Activates a given Pack instance, creates compression file
        """
        self._generate_directory_copy(file_paths)
        self._zip_files()

    def _configure(self, config):
        """ Configuration function for Pack

        Arguments:
            config {dict} -- configuration keys (includes command line args)
        """
        for key in config:
            setattr(self, key, config[key])
        self.comp_alt = self.component + '-alt'

    def _generate_directory_copy(self, file_paths):
        """ Creates a temporary directory for compression
        """
        comp_alt = self.component + '-alt'
        for name, path in zip(self.file_names, file_paths):
            copy_dir = join_paths([self.work_dir, comp_alt, name])
            copy_file(path, copy_dir)

    def _zip_files(self):
        """ Creates final compression and removes temporary directory
        """
        zip_path = join_paths([self.work_dir, self.zip])
        comp_alt_path = join_paths([self.work_dir, self.comp_alt])
        if path_exists(zip_path) and not self.override:
            terminate(
                "zip file {} exists, use -o to override existing copy".format(zip_path))
        # zip included in the archiving
        zip_dir(comp_alt_path, base_file_name(zip_path))
        delete_directory(comp_alt_path)
