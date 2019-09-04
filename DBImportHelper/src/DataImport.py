import os


# import pandas as pd

class DataImport:

    def __init__(self, fileName, fileType):
        self.fileName = fileName
        self.dataPath = "{}/data".format(os.path.dirname(os.path.dirname(__file__)))

    def _fileimporter(self, fileType):
        if fileType == 'excel':
            pass
        else:
            raise Exception('Invalid')

    def importFile(self):
        return self.fileName

    def checkIFFileExists(self):
        return os.path.exists(self.dataPath)

    def fullDataPath(self):
        return self.dataPath

    def convertToDataFrame(self, type):
        pass

if __name__ == '__main__':
    pass