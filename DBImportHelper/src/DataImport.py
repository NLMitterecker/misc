import os

class DataImport:

    def __init__(self, fileName):
        self.fileName = fileName
        self.dataPath = "{}/data".format(os.path.dirname(os.path.dirname(__file__)))

    def importFile(self):
        return self.fileName

    def checkIFFileExists(self):
        return os.path.exists(self.dataPath)

    def fullDataPath(self):
        pass


if __name__ == '__main__':
    pass