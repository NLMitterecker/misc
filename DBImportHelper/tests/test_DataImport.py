#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Daniel Mitterecker <daniel.mitterecker@gmail.com>"
__copyright__ = "Copyright 2019 by Daniel Mitterecker"
__licence__ = "GNU General Public License version 3 or later (GPLv3+)"

import os, sys

script_path=os.path.dirname(os.path.dirname(__file__))
full_src_path = os.path.dirname(os.path.join(script_path, "src/"))
full_data_path = os.path.dirname(os.path.join(script_path, "data/"))
sys.path.append(full_src_path)

import unittest
import DataImport as DI

class TestDataImport(unittest.TestCase):

    def setUp(self):
        self.testFile = 'testdata.xls'
        self.fullTestFilePath = "{}/{}".format(full_data_path, self.testFile)

    def test_importFileName(self):
        self.importer = DI.DataImport(self.fullTestFilePath)
        self.assertIsInstance(self.importer.importFile(), str)

    def test_checkFileExists(self):
        self.importer = DI.DataImport(self.fullTestFilePath)
        self.assertTrue(self.importer.checkIFFileExists())

    def test_fullDataPath(self):
        self.importer = DI.DataImport(self.fullTestFilePath)
        self.assertIsInstance(self.importer.fullDataPath(), str)

    def test_failingFileImporter(self):
        self.fileType = 'bla'
        self.importer = DI.DataImport(self.testFile, self.fileType)
        with self.assertRaises(Exception):
            self.importer.fileImporter(self.fileType)

    def test_correctFileImporter(self):
        self.fileType = 'excel'
        self.importer = DI.DataImport(self.testFile, self.fileType)
        obj = self.importer.fileImporter()
        self.assertIsNotNone(1)


if __name__ == '__main__':
    unittest.main()