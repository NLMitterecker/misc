import os, sys
config = {
    "tests_dir": "tests/",
    "src_dir": "src/"
}

script_path=os.path.dirname(os.path.realpath(__file__))
full_src_path = os.path.dirname(os.path.join(script_path, config['src_dir']))
full_tests_path = os.path.dirname(os.path.join(script_path, config['tests_dir']))

sys.path.append(full_src_path)
sys.path.append(full_tests_path)

import DataImport as DI
from tests import *

def run():
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "test":
            pass
        else:
            pass
    else:
        importer = DI.DataImport("testfile.xls")
        print("Hello {}".format(importer.importFileName()))

if __name__ == '__main__':
    run()