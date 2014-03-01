import sys
import keywords.py

if __name__ == '__main__':
	filename = sys.argv[1]
	file = open(filename)
	characters = file.read()
	file.close()
