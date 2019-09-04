#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase

__author__ = "Daniel Mitterecker <daniel.mitterecker@gmail.com>"
__copyright__ = "Copyright 2019 by Daniel Mitterecker"
__licence__ = "GNU General Public License version 3 or later (GPLv3+)"

import os, sys

script_path = os.path.dirname(os.path.dirname(__file__))
full_src_path = os.path.dirname(os.path.join(script_path, "src/"))
full_data_path = os.path.dirname(os.path.join(script_path, "data/"))
sys.path.append(full_src_path)

import unittest
import DataImport as DI
import pandas


class TestDataImport(unittest.TestCase):

    def setUp(self):
        self.testFile = 'testdata.xls'
        self.fullTestFilePath = "{}/{}".format(full_data_path, self.testFile)

    def test_importFileName(self):
        importer = DI.DataImport(self.testFile)
        self.assertIsInstance(importer.importFile(), str)

    def test_checkFileExists(self):
        importer = DI.DataImport(self.testFile)
        self.assertTrue(importer.checkIFFileExists())

    def test_fullDataPath(self):
        importer = DI.DataImport(self.testFile)
        self.assertIsInstance(importer.fullDataPath(), str)

    def test_failingFileImporter(self):
        importer = DI.DataImport(self.testFile, 'bla_filetype.plz')
        with self.assertRaises(Exception):
            importer.convertToDataframe()

    def test_correctFileImporter(self):
        self.fileType = 'excel'
        importer = DI.DataImport(self.testFile, self.fileType)
        self.assertIsNone(importer.convertToDataframe())

    def test_headDataFrame(self):
        self.fileType = 'excel'
        importer = DI.DataImport(self.testFile, self.fileType)
        importer.convertToDataframe()
        self.assertIsInstance(type(importer.headDataFrame()), type(pandas.core.frame.DataFrame))

    def test_generateSQLStatement(self):
        self.fail()

if __name__ == '__main__':
    unittest.main()
