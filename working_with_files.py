#!/usr/bin/python
import random
save_result=open("save.result","a+")
want_save="yes"
while want_save == "yes":
    random_number = random.randrange(1, 100)
    want_save=raw_input("Does you want save the result? (yes/no)")
    save_result.write(str(random_number)+"\n")
save_result.close()
