'''
In 1937, a German mathematician named Lothar Collatz formulated an intriguing
 hypothesis (it still remains unproven) which can be described
 in the following way:

    1. take any non-negative and non-zero integer number and name it c0;
    2. if it's even, evaluate a new c0 as c0 ÷ 2;
    3. otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
    4. if c0 ≠ 1, skip to point 2.

The hypothesis says that regardless of the initial value of c0,
 it will always go to 1.

Created on 2023 Dec 24

@author: ooleon
'''

def collatz(number):
	list=[]
	list.append(number)
	while number!=1:
		if	number%2==0:
			number=number//2
		else:
			number=number*3 + 1
		list.append(number)
	return list


for i in range(1, 110):
	print(collatz(i))
