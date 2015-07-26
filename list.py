#!/usr/bin/python
import random
'''
guess = random.randrange(1,3)
answer = 0

while answer!= guess:
    answer = int(raw_input("[*] Guess the number > "))
    if answer> guess:
        print "[-] the answer is bigger then the real number"
    elif answer<guess:
        print "[-] the answer is lower then the real number"
    else:
print "[+] you win :)"
'''

random_number = random.randrange(1, 3)
set_guess = 0
user_number = [set_guess]
#user_number.append(set_guess)
i = 0
while random_number != user_number:
    set_guess = int(raw_input("GUESS!"))
    user_number[set_guess]
   if user_number[i] > random_number:
     print "your number is bigger. "
    elif user_number[i] < random_number:
        print "your number is smaller. "
    i += 1
#print "you win!", "random_number = ", random_number
#print len(user_number)
