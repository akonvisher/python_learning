# /usr/bin/python
pre_number = raw_input("Enter your number or P for print the all: ")
number = []
number.append(pre_number)
while number[~0] != 'p':
    pre_number = raw_input("Enter your number or P for print the all: ")
    if pre_number in number:
        print 'This number is already there!'
    else:
        number.append(pre_number)
number.remove('p')
# print (number[0:-1])
# del number[~0]
print (number)
