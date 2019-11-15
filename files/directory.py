import os
# import sys
import glob

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))

class Directory(object):

	PATH = os.path.realpath(os.path.join(CURRENT_PATH, "../data/"))
	FILE_PATTERN = "*"
	files = []

	def __init__(self, path=None):
		self.path = path or self.PATH
		self.read()

	def read(self):
		glob_pattern = "{}/{}".format(self.path, self.FILE_PATTERN)
		self.files = glob.glob(glob_pattern)
		return self.files

	def each_file(self, callback):
		if not callback: return
		if not self.files: self.read()
		for path in self.files:
			with open(path) as f:
				callback(f)
