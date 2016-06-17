import csv
import sys
infile = sys.stdin
if len(sys.argv) > 1:
    infile = open(sys.argv[1])

with infile as f:
    reader = csv.reader(f)
    headers = reader.next()
    for idx, row in enumerate(reader):
        print "\nNEW RECORD = " + str(idx + 1) + "\n"
        for idx, header_val in enumerate(headers):
            print header_val + ':' + ' ' * (20 - len(header_val)) + row[idx]
