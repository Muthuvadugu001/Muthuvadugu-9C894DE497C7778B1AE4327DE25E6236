#write a Program that det#write a Program that determines whether a year entered by the user is a leap year or not using ifelif-else statements.

def isleapyear(year):
   if ( year % 4 == 0 and year % 100 != o) or year % 400==0:
     return True 
   else:
     return False
year = int(input ("enter a year: "))
if isleapyear(year):
   print('{} is a leap year.',format(year))
else:
  print('{} is a not a leap year.',format(year))