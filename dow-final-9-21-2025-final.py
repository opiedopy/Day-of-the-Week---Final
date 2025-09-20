"""Day of Week (DOW) Calculation (Years 9/14/1752 to 2800)
-may 18 2025 modification by ME for quicker calcs
I choose therefore to start my algorithm in 1753.  Calculations beyond 2800 are debatable.
___new method taken from YouTube internet, "BE SMART" "How to figure out DOW..."__by John H Conway
Day of Week (DOW) = [CC + AA + BB + DD + EE]
for any year
(DOW is a number from 0 to 6, Sunday thru Saturday)
Input is Day/Month/CCYY where CC is century and YY is last two digits, e.g. 2025

CC: Century# is           1700   1800   1900
                   2000   2100   2200   2300
                   2400   2500   2600   2700  etc etc
              ---------------------------------------
                    2      0      5       3
Note the 400 year repetition.

AA.  int(YY/12)
BB.  YY modulo 12
CC.	 Century # from table
DD.  int(BB/4)
EE.	 (day + monthx) mod 7

      monthx numbers (Note: I prefer not to use the author's "Doomsday" term)

      Note: leap year in ()
      monthx =         Jan  4 (3),  Feb 0 (6),   Mar 0,   Apr  3,
                       May  5,      Jun  1,      Jul 3,   Aug  6,
                       Sep  2,      Oct  4,      Nov 0,   Dec  2 
"""

# input date
out_of_range = 0
m = int(input("Month 1 to 12?  "))
if m>12:
    out_of_range = 1
    
day = int(input("Day 1 to 31? "))
if day>31:
    out_of_range = 1
if day>30 and (m==9 or m==4 or m==6 or m==11):
    out_of_range = 1
if day>29 and m==2:
    out_of_range = 1
    
y = int(input ("Year (XXXX format) ? "))
if y<1753 or y>2800:
    out_of_range = 1
    
#find last 2 digits of year, modulo 7
last3digitsofyear = (y%1000)
last2digitsofyear = (last3digitsofyear%100)

#
AA = int(last2digitsofyear/12)
BB = (last2digitsofyear%12)
DD = int(BB/4)


#determine leap year, returns leap = 1
leap = 0
y_m = (y%4)
y_m_400 = (y%400)
y_m_100 = (y%100)
if ((y_m_400 != 0) and (y_m_100 == 0)):
    leap = 0     #("year is not a leap year.")
    
elif y_m == 0:
    leap = 1     #("year is a leap year.")
   
else:
    leap = 0     #("year is not a leap year.")
    
#Month number program, adj for leap year
monthx = 0
if out_of_range == 0: 
    if leap == 1 and m == 1:
        monthx = 3
    elif leap == 1 and m == 2:
        monthx = 6
    else:
        monthnumlist = (4,0,0,3,5,1,3,6,2,4,0,2)
        monthx = (monthnumlist[m-1])

EE = (day + monthx)
    
#century
century = y - y_m_100
century_xx_m4 = int((century/100)%4)
centurylist = (2,0,5,3)   
century_num = (centurylist[century_xx_m4])
CC = century_num

# DOW number
dow_nu = AA+BB+CC+DD+EE
dow_num = dow_nu%7

#check for out of range
if m==2 and day==29 and leap==0:
    print("Invalid data since no February 29th that year")
elif out_of_range == 1:
    print ("data out of range, correct the date or use year  >1752 or <2800")
else:
    dowlist = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
           "Friday", "Saturday", "Sunday")
#convert day of week # to string name and print answer - Table 3
    print ("DOW = ",dowlist[dow_num])

#Individual Data Results that produce DOW
    print(" ")
    print("The following is the data used to determine the DOW = ",dowlist[dow_num])
    print(" The goal is to do all this in your head.  It is possible. I can do it.")
    print ("CC = year # (century             ",CC)
    print ("AA. = int(YY/12)                 ",AA)
    print ("BB. = YY mod 12                  ",BB)
    print ("DD = BB mod 4                    ",DD)
    print ("day =",day)
    print ("monthx = ",monthx)
    print ("EE. = (day + monthx)             ",EE)
    print ("Sum of AA+BB+CC+DD+EE =          ",dow_nu)
    print (dow_nu,"modulo 7 = DOW number =        ",dow_num,"or",dowlist[dow_num])
    if m>12 or day>31 or y<1753 or y>9999:
        print ("Date may be wrong because, out of range")
    print("Sun Mon Tue Wed Thu Fri Sat")
    print(" 0   1   2   3   4   5   6")
    print("Note: m-d-y was                   ",m,"-",day,"-",y)
    
   

""" REFERENCE
All of the above can be memorized and performed mentally for an audience. 30 seconds or less!

NOTE: This DOW method gives results that agree with all other methods on the internet for
Gregorian dates. Gregorian is what the USA and almost all nations use.The Julian Calendar was replaced,
in the USA in 1752,
by the Gregorian Calendar, changing the formula for calculating leap years. The beginning of the legal new year
was moved from March 25 to January 1.  11 days were dropped from the month of September 1752.
Also, beware of something called the “Revised Julian Date” method. That method is rare and
agrees with Gregorian only until the
year 2800, but Wikipedia Experts will disagree on dates after 2800.
There is also a revised Gregorian calendar under consideratrion after 2800.
I found one source that said that in the distant
future, a whole day may need to be added, thereby, making this program inaccurate in a couple of thousand years. :-)
And a different method was used by many countries prior to 1752, so this program does not work <1753.

Leap Year:
To use table 1, and if your month is January or February, you must memorize
the rules for all LEAP YEARS!!
Except for case below, if a year is divisible by 4 it is a leap year:
Examples: 1952, 2016, 2020, 2024, 2096, 2548 are all leap years since they
are divisible by 4.
- A year divisible by 100, but not 400, is not a leap year, so
1900, 2100, 2200, 2300, 2700 are not leap years since they are
divisible by 100 but not 400. 1600 and 2000 and 2400 are leap years.
"""