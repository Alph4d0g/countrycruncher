import argparse

parser = argparse.ArgumentParser()
parser.add_argument("inputfile", help="Place you source file here")
parser.add_argument("outputfile", help="Place you destination file here")
args = parser.parse_args()

with open('countrylist.csv', 'r') as countries:
    ccs = countries.read().splitlines()
with open(args.inputfile, 'r') as original:
    with open(args.outputfile, 'w') as output:
        for number in original:
            if not number.isspace():
                if number.startswith("00"):
                    number = number[2:]
                    nsn = number[len(filter(number.startswith,tuple(ccs+['']))[0]):]
                    cc = number[:-len(nsn)]
                    output.write(cc+","+nsn)
