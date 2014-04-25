#!/usr/bin/env python
# encoding: utf-8
"""
basics.py

Created by Adam Beguelin on 2014-04-21.
Copyright (c) 2014 Beguelin Ventures. All rights reserved.
"""

import sys
import os


def main():
	print 'Simple Assignment'
	shoplist = ['apple', 'mango', 'carrot', 'banana']
	# mylist is just another name pointing to the same object!
	mylist = shoplist

	# I purchased the first item, so I remove it from the list
	del shoplist[0]

	print 'shoplist is', shoplist
	print 'mylist is', mylist
	# Notice that both shoplist and mylist both print
	# the same list without the 'apple' confirming that
	# they point to the same object

	print 'Copy by making a full slice'
	# Make a copy by doing a full slice
	mylist = shoplist[:]
	# Remove first item
	del mylist[0]

	print 'shoplist is', shoplist
	print 'mylist is', mylist
	# Notice that now the two lists are different

if __name__ == '__main__':
	main()

