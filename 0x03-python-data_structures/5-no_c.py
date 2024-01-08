#!/usr/bin/python3
def no_c(my_string):
    if my_string [:]:
        nstring = my_string.translate({ord("c"): None})
        nstring2 = my_string.translate({ord("C"): None})
        return nstring2
    return my_string
