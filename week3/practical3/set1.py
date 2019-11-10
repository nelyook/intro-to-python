import argparse
parser= argparse.ArgumentParser ()
parser.add_argument ("number", help= "add number", type = int)
args= parser.parse_args()
set1 = {2,3,4,5,6,7}
print (set1)
set1.add (args.number)
print (set1)