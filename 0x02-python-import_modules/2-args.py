#!/usr/bin/python3
if __name__ == "__main__":
   from sys import argv
   c = len(argv) - 1
   if c < 1:
        print("{} arguments.".format(c))
   elif c == 1:
        print("{} arguments:".format(c))
   else:
        print("{} arguments:".format(c))
   for i in range(c):
        print("{}: {}".format(i + 1, argv[i + 1]))
