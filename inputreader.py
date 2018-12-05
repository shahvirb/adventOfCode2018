import os

BASE_DIR = r'inputs'

def read2018(input2018):
    return readfile(os.path.join(BASE_DIR, input2018))


def readfile(path):
    with open(path, 'r') as file:
        return file.read()
