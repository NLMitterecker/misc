import unittest
from DataImport import DataImport

class TestDataImport(unittest.TestCase):

    def setUp(self):
        pass

    def test_importFileName(self):
        pass
        importer = DataImport("FileName")
        self.assertIsInstance(importer.importFileName(), str)

if __name__ == '__main__':
    unittest.main()