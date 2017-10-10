myPrimeList =[]
min_num = 0
max_num = int(input("Enter your the number within which you want prime numbers:"))
for x in range (min_num,max_num+1):
  if x > 1:
       for y in range(2,x):
           if (x % y) == 0:
               break
       else:
           myPrimeList.append(x)
print(myPrimeList)
      
