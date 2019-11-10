import argparse
parser= argparse.ArgumentParser ()
parser.add_argument ("remove", help= "remove 2", type = int)
args= parser.parse_args()
list4 = [2,3,4,5]
print (list4)
list4.remove (args.remove)
print (list4)