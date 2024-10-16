
def CheckLeap(Year):  
  
  if((Year % 400 == 0) or  # Checking if the given year is leap year  
     (Year % 100 != 0) and  
     (Year % 4 == 0)):   
    print("Given Year is a leap Year");  
  
  else:  
    print ("Given Year is not a leap Year")   # Else it is not a leap year 
 
Year = int(input("Enter the number: "))  
 
CheckLeap(Year)  