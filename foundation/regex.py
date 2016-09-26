import re
fname = raw_input('Enter the file name:')
if len(fname) <= 1:fname = 'regex_sum_42.txt'
fhandl = open(fname)
numlist = list()
for lines in fhandl:
    lines = lines.rstrip()
    #print lines
    lst = re.findall('[0-9]+',lines)
    for strnum in lst:
        try:
            num = int(strnum)
            numlist.append(num)
        except:
            print "the strnum is not right!", strnum

print sum(numlist)