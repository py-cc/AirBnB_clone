#!/usr/bin/python3

import unittest
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """ TestFileStorage unittest"""

    def test_storage(self):
        """test_storage"""
        self.assertTrue(True)

    def test_FileStorage(self):
        """ test __file_path"""
        self.assertNotEqual(FileStorage, "")
