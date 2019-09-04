from DataImport import DataImport

def run():
    importer = DataImport("testfile.xls")
    print("Hello {}".format(importer.importFileName()))

if __name__ == '__main__':
    run()