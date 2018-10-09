#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Matheus Rocha Vieira"
__version__ = "0.0.1"
__license__ = "GNU GPLv3"

import argparse
import numpy as np
from algorithms import *


def main(args):
	""" Main entry point of the app """
	unsorted_array = []

	if args.order == 'ASC':
		unsorted_array = list(range(0, int(args.instancesize)))

	if args.order == 'DESC':
		unsorted_array = list(range(0, int(args.instancesize)))
		unsorted_array = list(reversed(unsorted_array))

	if args.order == 'RAND':
		unsorted_array = list(range(0, int(args.instancesize)))
		np.random.shuffle(unsorted_array)

	size = int(args.instancesize)

	if args.algorithm == 'all':
		selection_sort(unsorted_array, size)
		insertion_sort(unsorted_array, size)
		shell_sort(unsorted_array, size)
		merge_sort(unsorted_array, size)
		heap_sort(unsorted_array, size)
		quick_sort(unsorted_array, size)

	if args.algorithm == 'selection':
		selection_sort(unsorted_array, size)

	if args.algorithm == 'insertion':
		insertion_sort(unsorted_array, size)

	if args.algorithm == 'shell':
		shell_sort(unsorted_array, size)

	if args.algorithm == 'merge':
		merge_sort(unsorted_array, size)

	if args.algorithm == 'heap':
		heap_sort(unsorted_array, size)

	if args.algorithm == 'quick':
		quick_sort(unsorted_array, size)

if __name__ == "__main__":
	""" This is executed when run from the command line """
	parser = argparse.ArgumentParser()

	parser.add_argument(
		"-alg",
		"--algorithm",
		choices=['all','selection', 'insertion', 'shell', 'merge', 'heap', 'quick']
	)

	parser.add_argument(
		"-is",
		"--instancesize",
		choices=['10', '1000', '100000', '1000000']
	)

	parser.add_argument(
		"-o",
		"--order",
		choices=['ASC', 'DESC', 'RAND']
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
