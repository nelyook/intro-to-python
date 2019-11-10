import argparse
parser= argparse.ArgumentParser ()
parser.add_argument ("number", help= "add number", type = int)
args= parser.parse_args()
set2 = {2,3,4,5,6,7,8,9}
print (set2)
set2.remove(args.number)
print (set2)