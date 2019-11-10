import argparse
parser = argparse.ArgumentParser()
parser.add_argument ("number", help = "number of 3s", type =int)
args = parser.parse_args()
list2 = [1, 3, 5, 3]
number = list2.count (args.number)
print ( 'the list:', list2 )
print ( "the number of element:", number)