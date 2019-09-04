from src import DataImport as DI
from tests import *
import os, sys

def run():
    if len(sys.argv) > 1:
        # TODO implemente argparse module
        importer = DI.DataImport(sys.argv[1])
        importer.convertToDataframe()
        print(importer.headDataFrame())
    else:
        raise Exception("No filename give as argument! Quitting.")

if __name__ == '__main__':
    run()