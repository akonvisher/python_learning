#!/usr/bin/python
import os
print "#############menu#############"
select_number = raw_input("enter 1 or 2 > ")
if select_number == "1":
    name=raw_input("please enter file name be created > ")
    touch="touch "+name
    ls="ls "+name
    if os.system(ls) == 0:
        print "the name exist"
    else:
        os.system(touch)
elif select_number == "2":
    name=raw_input("please enter folder name be created > ")
    ls="ls "+name
    if os.system(ls) == 0:
        print "the name exist"
    else:
        mkdir="mkdir "+name
        os.system(mkdir)
else:
    print "you entered wrong number!"