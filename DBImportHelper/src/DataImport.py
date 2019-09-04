import os
import pandas as pd

class DataImport:

    def __init__(self, fileName, fileType="excel"):
        self.fileName = fileName
        self.dataPath = "{}/data".format(os.path.dirname(os.path.dirname(__file__)))
        self.fileType = fileType

    def fileImporter(self):
        if self.fileType == 'excel':
            # TODO os.join in application; not concat!
            fullFilePath = "{}/{}".format(self.dataPath, self.fileName)
            return pd.read_excel(fullFilePath)
        else:
            raise Exception('Invalid')

    def importFile(self):
        return self.fileName

    def checkIFFileExists(self):
        return os.path.exists(self.dataPath)

    def fullDataPath(self):
        return self.dataPath

if __name__ == '__main__':
    pass