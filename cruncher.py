import sys
import re
glob_SingleLine = None
index = None

testvalue = "123456789"


def checkcountry(string):
    if re.match("^1.*", string):
        cc = "1"
        nsn = string[1:]
        return 
    elif string.startswith("49"):
        print "Country is GERMANY"
        cc = "49"
        nsn = string [2:]
        print nsn

checkcountry(testvalue)

with open('testfile.csv', 'r') as original:
    for index in original:
        if not index.isspace():
            if index.startswith("00"):
                index = index[2:]
                checkcountry(index)
            else:
                checkcountry(index)



print (original.closed)
