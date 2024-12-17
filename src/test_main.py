import unittest
from main import *

class Teststatictopublic(unittest.TestCase):
	def testpathexists(self):
		print(static_to_public("/home/gavril/workspace/github.com/gavril-do/boot.dev_generator/static"))