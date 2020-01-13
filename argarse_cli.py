import argparse
import sys

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("--x", type=float, default=1.0,
		help="What is the first number?")
	parser.add_argument("--y", type=float, default=1.0,
		help="What is the second number?")
	parser.add_argument("--operation", type=str, default="add",
		help="What operation? (add, mul, sub, div)")
	args = parser.parse_args()
	print(calc(args))

def calc(args):
	if args.operation == "add":
		return args.x + args.y
	if args.operation == "sub":
		return args.x - args.y
	if args.operation == "mul":
		return args.x * args.y
	if args.operation == "div":
		return args.x / args.y

# Use this file in the form of python argparse_cli.py --x=2 --y=8 --operation=mul

if __name__ == "__main__":
	main()