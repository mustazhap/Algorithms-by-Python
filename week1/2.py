import math

summ = int(input("Enter SUM of numbers: "))
product = int(input("Enter PRODUCT of numbers: "))
'''
*** x * y = product
*** x + y = sum
*** x = sum - y
*** (sum - y) * y = product
*** sum*y - y*y = product | y^2 - sum*y + product = 0
*** Descr = b^2 - 4ac; y1 = (-b +sqrt(D))/2a
***                    y2 = (-b -sqrt(D))/2a
*** x1 = sum - y1
*** x2 = sum - y2
'''

Descr = summ*summ - (4* product)
y1 = ( summ + math.sqrt(Descr))/2
y2 = ( summ - math.sqrt(Descr))/2
x1 = summ - y1
x2 = summ - y2

print("Answer: ",x1, " and ", y1)




        
        
