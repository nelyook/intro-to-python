import argparse
parser = argparse.ArgumentParser ()
parser.add_argument ("--age", type=int)
args = parser.parse_args()
if args.age:
    print ("Happy Birthday you are already " + str(args.age) + " years old!")
