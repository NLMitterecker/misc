from src import DataImport as DI
from tests import *

def run():
    importer = DI.DataImport("testfile.xls")
    print("Hello {}".format(importer.importFileName()))

if __name__ == '__main__':
    run()