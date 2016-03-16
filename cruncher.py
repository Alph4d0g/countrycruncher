import argparse
from itertools import groupby
from operator import itemgetter
import sys
sys.setrecursionlimit(10000)

parser = argparse.ArgumentParser()
parser.add_argument("inputfile", help="Place you source file here")
parser.add_argument("outputfile", help="Place you destination file here")
args = parser.parse_args()



def genblocks(group):
    blocked = []
    baseblocks = [i for i,x in enumerate(group) if (int(x[1])%10) == 0]
    if len(baseblocks)>0:
        if baseblocks[0]>0: blocked.extend(group[:baseblocks[0]])
        for block in baseblocks:
            if ((len(group)-block+1)>=10):
                blocked.append([group[block][0],group[block][1][:-1]])
            else:
                blocked.extend(group[block:])
    if len(baseblocks)>=10:
        return genblocks(blocked)
    else:
        return blocked

def genallblocks(data):
    ranges = []
    for k, g in groupby(enumerate(data), lambda (i,x):i-(int(x[0])+int(x[1]))):
        group = map(itemgetter(1), g)
        blocks = []
        if len(group)>9:
            blocks = genblocks(group)
        else:
            blocks = group
        ranges.extend(blocks)
    return ranges





with open('countrylist.csv', 'r') as countries:
    ccs = countries.read().splitlines()
with open(args.inputfile, 'r') as original:
    with open(args.outputfile, 'w') as output:
        data = []
        for number in original:
            if not number.isspace():
                if number.startswith("00"):
                    number = number[2:]
                    nsn = number[len(filter(number.startswith,tuple(ccs+['']))[0]):]
                    cc = number[:-len(nsn)]
                    data.append([cc,nsn])
        for block in genallblocks(data):
            output.write(block[0]+","+block[1])
