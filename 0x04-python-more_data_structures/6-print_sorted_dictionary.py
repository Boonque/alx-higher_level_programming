#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_ord = list(a_dictionary.keys())
   st_ord.sort()
   for i in list_ord:
       print("{}: {}".format(i, a_dictionary.get(i)))
