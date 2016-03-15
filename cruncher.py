import argparse


parser = argparse.ArgumentParser()
parser.add_argument("inputfile", help="Place you source file here")
parser.add_argument("outputfile", help="Place you destination file here")
args = parser.parse_args()




print "Begin"
with open('countrylist.csv', 'r') as countries:
    print "Countries imported"
    ccs = countries.read().splitlines()
    print ccs[1]

with open(args.inputfile, 'r') as original:
    with open(args.outputfile, 'w') as output:

        print "testfile opened"
        for number in original:
            if not number.isspace():
                if number.startswith("00"):
                    number = number[2:]
                    nsn = number[len(filter(number.startswith,tuple(ccs+['']))[0]):]
                    cc = number[:-len(nsn)]
                    output.write(cc+","+nsn)

print (output.closed)
print (original.closed)
