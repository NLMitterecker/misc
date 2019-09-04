import os
import pandas as pd
import sqlalchemy

class DataImport:

    # TODO use object for settings in constructor
    def __init__(self, fileName, fileType="excel"):
        self.fileName = fileName
        self.dataPath = "{}/data".format(os.path.dirname(os.path.dirname(__file__)))
        self.fileType = fileType

    def convertToDataframe(self):
        if self.fileType == 'excel':
            # TODO os.join in application; not concat!
            fullFilePath = "{}/{}".format(self.dataPath, self.fileName)
            self.dataFrame = pd.read_excel(fullFilePath)
        else:
            raise Exception('Invalid file type!')

    def importFile(self):
        return self.fileName

    def checkIFFileExists(self):
        return os.path.exists(self.dataPath)

    def fullDataPath(self):
        return self.dataPath

    def headDataFrame(self):
        return self.dataFrame.head()

    def generateSQLStatement(self):
        pass

    def mergeDataFrameColumns(self, *args):
        pass

    def generateDataSetStatistics(self):
        pass

if __name__ == '__main__':
    pass