from os import path

from django.contrib.staticfiles.finders import BaseFinder
from django.conf import settings


class StaticRootFinder(BaseFinder):
    """
    A static files finder to find files in the STATIC_ROOT directory
    """

    def find(self, file_path, all=False):
        base_dir = getattr(settings, 'BASE_DIR', '')
        static_root = getattr(settings, 'STATIC_ROOT', '')
        static_root_file_path = path.join(base_dir, static_root, file_path)

        if all:
            raise NotImplementedError("'all' not implemented")

        if path.isfile(static_root_file_path):
            return static_root_file_path
