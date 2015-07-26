#!/usr/bin/python

import pickle

a1= "roman"
a2 = 1
a3 = [1,2,3,4,5]

new = open("save.lst","w")
pickle.dump([a1,a2,a3],new)
new.close()


new = open("save.lst","r")
a1,a2,a3 = pickle.load(new)
print a1,a2,a3
print a3[1]
