Determining the day of the week
====================================
Zeller's Congruence
---------------------
Code to determine the day of the week based on dd,mm,yyyy inputs. 
The program is based on Zeller's congruence - https://en.wikipedia.org/wiki/Zeller%27s_congruence
Gregorian calendar is calculated as:

> h = (q + [13(m+1)/5] + K + K/4 + J/4 + 5*J ) mod 7

> where

> h is the day of the week (0 = Saturday, 1 = Sunday, 2 = Monday, ..., 6 = Friday)

> q is the day of the month

> m is the month (3 = March, 4 = April, 5 = May, ..., 14 = February. January, the first month would count as the 13th month of the previous year)

> K is year mod 100

> J is the zero based century. This is determined by floor division i.e. year / 100 and determines the century -19 in 1995, 20 in 2017

Doomsday rule
------------------
> https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week#The_%22doomsday%22
> https://en.wikipedia.org/wiki/Doomsday_rule

Sakamoto's Algorithm
------------------------
> dayofweek(y, m, d)	/* 1 <= m <= 12,  y > 1752 (in the U.K.) */

> {

>    static int t[] = {0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4};

>    if ( m < 3 )

>    {

>        y -= 1;

>    }

>    return (y + y/4 - y/100 + y/400 + t[m-1] + d) % 7;

> }

Explanation
---------------
The knowns:
1. Jan 1st 1 AD is a Monday in Gregorian calendar
2. February of 1 AD will start 3 days ahead
3. Every 4 years will be a leap year (exceptions to the rule, we will come to those later)
4. February will have 28 days for non-leap years. March and February will start on the same day in these years
5. There are 365 days in a non-leap year

Steps to arrive at the day of the week:
Let us consider the first case in which we do not have leap years i.e days = 365. 
January has 31 days i.e 7*4+3 days so the day on 1st Feb will always be 3 days ahead of the day on 1st January. 
Now february has 28 days(excluding leap years) which is exact multiple of 7 (7*4=28). March will also start on the same day as February. 
Considering this pattern, if we create an array of the leading number of days for each month then it will be given as t[] = {0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5}. 

Now let us look at the real case when there are leap years. Every 4 years, our calculation will gain one extra day. 
The exception to the rule is that every 100 years when it doesn’t. The exception to this 100 year rule is that every 400 years when it does. 

How do we calculate these additional days? Just add y/4 – y/100 + y/400. The division is integer division / floor division. 
This adds exactly the required number of leap days.
It would have been easy if the day was added at the end of the year (i.e. a Dec 32nd or a 0 Jan). The extra day is always in February. So it would occur after the 13th month.
This also means that current year should not be calculated for the leap day calculation, for the months of Jan and Feb. i.e. the y/4 value would be that of the previous year and would not be counted. 
To achieve this, we instead deduct i day from the array t[] for every month after Feb.
So the revised array is t[] = {0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4}.
If the month (m) corresponds to Jan/Feb (that is, month<3) we decrement y by 1. 
y in turn becomes y + y/4 – y/100 + y/400
