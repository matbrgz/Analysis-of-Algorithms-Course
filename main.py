#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Matheus Rocha Vieira"
__version__ = "0.0.1"
__license__ = "MIT"

import argparse
import tools.instancegenerator

def main(args):
	""" Main entry point of the app """


if __name__ == "__main__":
	""" This is executed when run from the command line """
	parser = argparse.ArgumentParser()

	parser.add_argument(
		"-alg",
		"--algorithm",
		choices=[
			'selectiondort', 'insertionsort', 'shellsort', 'mergesort'
		]
	)
				
	parser.add_argument(
		"-is",
		"--instancesize",
		choices=[
			10, 1000, 100000, 1000000
		]
	)

	parser.add_argument(
		"-o",
		"--order",
		choices=[
			'ASC', 'DESC', 'RAND'
		]
	)

	parser.add_argument(
		"--verbose",
		action="count",
		default=0,
		help="Verbosity"
	)

	parser.add_argument(
		"-v",
		"--version",
		action="version",
		version="%(prog)s (version {version})".format(version=__version__)
	)

	args = parser.parse_args()
	main(args)
