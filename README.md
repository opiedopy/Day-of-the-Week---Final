# Day-of-the-Week---Final
Day of Week (DOW) Calculation (Years 1753 to 9999)

September 16 2025 modification by Jackie Dander, fuzzywidget.com

Copyright.  May be used with attribution.

Day of Week (DOW) = [AA + BB + CC + DD + EE + FF] for any year

or Item 1 + 2 + 3 + 4 + 5 + 6

(DOW is a number from 0 to 6, Sunday thru Saturday)

Input is Day/Month/CCYY where CC is century and YY is last two digits, e.g. 2025


1. or
   
AA.	 month_val

      Note: leap year in ()
      
      month_val =   Jan 4(3), Feb 0(-1), Mar 0, Apr 3, May 5, Jun 1, Jul 3, Aug 6, Sep 2, Oct 4, Nov 0, Dec 2
      
____________________________    
2. or
                       
BB.  day 
____________________________ 

3. or
   
CC:  Century# 

1600    2

1700    0

1800    5

1900    3 

2000    2

2100    0 

2200    5

2300    3

2400    2

2500    0

2600    5

2700    3

etc 

etc

7600    2

7700    0

7800    5

7900    3


Note the 400 year repetition beginning at 1600 (and 2000, 2400, 3600, 5200 etc.)  Example year 7783 has CC of 0.  Year 4467 has CC of 2, because 4400 century is divisible by 400.
____________________________ 

4.or

DD.  int(YY/12), means integer and no fractions
____________________________ 

5. or
 
EE.  YYmod12, mod means modulo and is espressed YY%12

____________________________ 
6. or

FF.  int(EE/4)

____________________________ 

Examples:
February 29, 2052
-Is a leap year, therefore:
1. month_val       = -1
2. day             = 29
3. CC              =  2
4. int(YY/12)      =  4
5. YY%12           =  4
6. int((YY%12)/4)  =  1
   sum             = 39, 39 modulo 7 = 4, 39%7 = 4
   day of week (DOW) is therefore Thursday
   
October 30, 2027
1. month_val       =  4
2. day             = 30
3. CC              =  2
4. int(YY/12)      =  2
5. YY%12           =  3
6. int((YY%12)/4)  =  0
   sum             = 41, 41 modulo 7 = 6, 41%7 = 6
   day of week (DOW) is therefore Saturday
   
 June 18, 7932
1. month_val       =  1
2. day             = 18
3. CC              =  3
4. int(YY/12)      =  2
5. YY%12           =  8
6. int((YY%12)/4)  =  2
   sum             = 34, 34 modulo 7 = 6, 34%7 = 6
   day of week (DOW) is therefore Saturday

     

""" REFERENCE
All of the above can be memorized and performed mentally for an audience. 30 seconds or less!

NOTE: This DOW method gives results that agree with all other methods on the internet for Gregorian dates. Gregorian is what the USA and almost all nations use. The Julian Calendar was replaced,in the USA in 1752, by the Gregorian Calendar, changing the formula for calculating leap years. 
11 days were dropped from the month of September 1752. 
The “Revised Julian Date” is out there but this method is not for civil use as timeanddate.com explains. It is used for some churches only.
There is also a revised Gregorian calendar under consideration after 2800 but no decision made yet. This program may be inaccurate in many centuries.

And the Gregorian Calendar was not adopted by all countries at one time  prior to 1752, so this program does not work <1753.

Leap Year:
To use the month_val table, and if your month is January or February, you must memorize  the rules for all LEAP YEARS!!
Except for case below, if a year is divisible by 4 it is a leap year:
Examples: 1952, 2016, 2020, 2024, 2096, 2548 are all leap years since they are divisible by 4.
But,
- A year divisible by 100, but not 400, is not a leap year, so
1900, 2100, 2200, 2300, 2700 are not leap years since they are
divisible by 100 but not 400. 1600 and 2000 and 2400 are leap years.

