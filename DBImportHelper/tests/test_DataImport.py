#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Daniel Mitterecker <daniel.mitterecker@gmail.com>"
__copyright__ = "Copyright 2019 by Daniel Mitterecker"
__licence__ = "GNU General Public License version 3 or later (GPLv3+)"

import os, sys
config = {
    "tests_dir": "tests/",
    "src_dir": "src/"
}

script_path=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
full_src_path = os.path.dirname(os.path.join(script_path, config['src_dir']))
full_tests_path = os.path.dirname(os.path.join(script_path, config['tests_dir']))

sys.path.append(full_src_path)
sys.path.append(full_tests_path)

import unittest
import DataImport as DI

class TestDataImport(unittest.TestCase):

    def setUp(self):
        pass

    def test_importFileName(self):
        importer = DI.DataImport("FileName")
        self.assertIsInstance(importer.importFileName(), str)

if __name__ == '__main__':
    unittest.main()