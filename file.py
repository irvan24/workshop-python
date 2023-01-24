
for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("ThreeFive")
    elif num % 3 == 0:
        print("Three")
    elif num % 5 == 0:
        print("Five")
    else:
        print(num)



def findSum(str1):

	temp = "0"
	Sum = 0

	for ch in str1:

		if (ch.isdigit()):
			temp += ch
		else:
			Sum += int(temp)
			temp = "0"

	return Sum + int(temp)

str1 = ["168", "4"]

print(findSum(str1))

from random import *

x = randint(1, 100)    # Pick a random number between 1 and 100.
print(x)
