from zipfile import ZipFile, BadZipFile
import itertools
from itertools import product
import string
import sys


zipfile = "crack.zip"
password = "crack".encode('ascii')
alphabet = string.ascii_lowercase


def attempt(zipfile, password):
    try:
        with myzip.open('file.txt', pwd=password) as myfile:
            # print(myfile.read())
            contents = myfile.read()
            return True
    except RuntimeError:
        return False
        #print("Wrong password!")
    except BadZipFile:
        return False


with ZipFile(zipfile) as myzip:
    # if attempt(myzip, password):
    #    print(f"Password is {password}")
    for password in itertools.product(alphabet, repeat=4):
        password = "".join(password).encode('ascii')
        if attempt(myzip, password):
            print(f"Password is {password}")
            with myzip.open('file.txt', pwd=password) as z:
                print(z.read())
                sys.exit(0)
