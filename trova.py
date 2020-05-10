#!/usr/bin/env python

import glob
import re
import os
import sys
import argparse

# Function to load in a variable all terms to be searched
#
# input: file name
# return: array
def loadSearches(fileName):
    toSearch = None
    with open(fileName) as origin_file:
        toSearch = origin_file.readlines()

    return toSearch

# Function search and count
#
# input:    fileName to search in
#           string 
# output:   occurrences
def howMany(fileName,stringSearch, case=False):
    with open(fileName) as search_file:
        counter = 0
        for line in search_file:
            if case:
                line = re.findall(r'^'+stringSearch+'$', line)
            else:
                line = re.findall(r'^'+stringSearch+'$', line,re.IGNORECASE)
            if len(line) > 0:
                counter += 1
    return counter


########################################################################
########################################################################
# MAIN
########################################################################
########################################################################

args = argparse.Namespace()
__version__ = "0.10"
__description__ = 'Search strings in files'

# Create argument parser
usage = '\r{}\nusage: %(prog)s -f <file_lista> -d <dir_logs> [-c <num>] [-s] | [-h] | [-v]' \
    .format('Version {version}'.format(version=__version__).ljust(len('usage: ')))

mypar = argparse.ArgumentParser(description=__description__, usage=usage,
                                formatter_class=argparse.RawTextHelpFormatter)

mypar.add_argument('-v', '--version', action='version',
                   version='%(prog)s v. {version}'
                   .format(version=__version__),
                   help='show program version')
mypar.add_argument('-c', type=int,action='store', dest='counter',default=1, help='numero minimo di occorrenze (0 = solo valori unici')
mypar.add_argument('-s', action='store_true', dest='Case', default=False, help='case sensitive')

required = mypar.add_argument_group('required arguments')
required.add_argument(
    '-f', '--file', help='<file_lista> file contenente le stringhe da cercare',
    required=True, default='', metavar='<file_lista>')
required.add_argument(
    '-d', '--dir', help='<directory> directory che contiene i file in cui cercare',
    required=True, default='', metavar='<directory>')

# check if arguments is passed, otherwise print help
if len(sys.argv) == 1:
    mypar.parse_args(['-h'])
else:
    args = mypar.parse_args()

if not os.path.exists(args.file):
    print("ERRORE: il file {} non esiste".format(args.file))
    sys.exit(1)
else:
    searchFileName = args.file

if not os.path.exists(args.dir):
    print("ERRORE: la directory {} non esiste".format(args.dir))
    sys.exit(1)
else:
    path = args.dir

limitOccurrences = args.counter
checkCase = args.Case

files = [f for f in glob.glob(path + "**/*", recursive=True)]

myList = loadSearches(searchFileName)

for k in files:
    for number, i in enumerate(myList):
        numOccurrences = howMany(k,i, checkCase)
        if numOccurrences == None:
            numOccurrences = 0
        if numOccurrences >= limitOccurrences and limitOccurrences > 0:
            print("{},{},{}".format(i.rstrip(),k,numOccurrences))
        if numOccurrences == limitOccurrences and limitOccurrences == 0:
            print("{},{},{}".format(i.rstrip(), k, numOccurrences))



