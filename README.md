# DayOfTheWeekDeterminant
Code to determine the day of the week based on dd,mm,yyyy inputs
The program is based on Zeller's congruence - https://en.wikipedia.org/wiki/Zeller%27s_congruence
Gregorian calendar is calculated as:
h = (q + [13(m+1)/5] + K + K/4 + J/4 + 5*J ) mod 7
where
h is the day of the week (0 = Saturday, 1 = Sunday, 2 = Monday, ..., 6 = Friday)
q is the day of the month
m is the month (3 = March, 4 = April, 5 = May, ..., 14 = February. January, the first month would count as the 13th month of the previous year)
K is year mod 100
J is the zero based century. This is determined by floor division i.e. year // 100 and determines the century -19 in 1995, 20 in 2017
