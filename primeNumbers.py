
def primeNumbers(num):
    myPrimeList = []
    for x in range (num+1):
        if x > 1:
            for y in range(2,x):
                if (x % y) == 0:
                    break
            else:
                myPrimeList.append(x)
    return myPrimeList

def enterNumber():
	max_num = int(input("Enter your the number within which you want prime numbers:"))
	return max_num
    
