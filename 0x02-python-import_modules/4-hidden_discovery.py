#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    every_f = dir()
    for i in range(0, len(every_f)):
        if every_f[i][:2]!= "__":
            print("{:s}".format(every_f[i]))
