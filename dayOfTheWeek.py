# -*- coding: utf-8 -*-
"""
1.t[] now becomes {0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4}. 
2.if m corresponds to Jan/Feb (that is, month<3) we decrement y by 1. 
3.the annual increment inside the modulus is now y + y/4 – y/100 + y/400 in place of y. 
"""
def day_of_the_week(y,  m, d) :
 
    # array with leading number of days values
    t = [ 0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4 ]
    
    # m is the month (3 = March, 4 = April, 5 = May, ..., 14 = February. January, the first month would count as the 13th month of the previous year)      
    # if month is less than 3 reduce year by 1
    if (m < 3) :
        y = y - 1
          
    return (y + y // 4 - y // 100 + y // 400 + t[m - 1] + d) % 7

def getKeysByValue(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] == valueToFind:
            listOfKeys.append(item[0])
    return  listOfKeys
     
weekdays =  {
            "Sunday" : 0        
            ,"Monday" : 1
            ,"Tuesday" : 2
            ,"Wednesday" : 3
            ,"Thursday" : 4
            ,"Friday" : 5
            ,"Saturday" : 6
            }
    
# Inputs
day = 1
month = 3
year = 2021
 
#print(day_of_the_week(year, month, day))
d = getKeysByValue(weekdays, day_of_the_week(year, month, day) )
print(day, month, year)
print(d[0])
