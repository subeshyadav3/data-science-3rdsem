import nepali_datetime as ndt
import datetime as dt
from english_to_nepali import english_to_nepali
from nepali_to_english import nepali_to_english
import os

def header():
    print("*************Welcome to the Date Conversion:**************")

def clearscreen():
   os.system('cls' if os.name=='nt' else 'clear')

def main():
 while True:
    clearscreen()
    header()
    print("\nDate Conversion Options")
    print("1). English To Nepali Date Conversion:")
    print("2). Nepali To English Date Conversion:")
    print("3). Exit")

    choice=input("Enter Your choice(1/2/3):")
    
    if choice=="1":
       
       print("Enter the English date in the format:(Year/Month/Day)")
        
       ad_year=int(input("Year:"))  
       ad_month=int(input("Month:"))
       ad_day=int(input("Day:"))


       nepali_date=english_to_nepali(ad_year,ad_month,ad_day)

       if isinstance(nepali_date,ndt.date):
            print(f"English date:{ad_year}/{ad_month}/{ad_day}")
            print(f"Nepali date: {nepali_date.strftime('%K-%n-%D')}")


       else:
         print("nepali_date")

    elif choice=="2":

            print("Enter the nepali date in the format:(Year/Month/Day)")

            bs_year=int(input("Year:"))  
            bs_month=int(input("Month:"))
            bs_day=int(input("Day:"))

            english_date=nepali_to_english(bs_year,bs_month,bs_day)

            if isinstance(english_date,datetime.date):
              print(f"Nepali date:{bs_year}/{bs_month}/{bs_day}")
              print(f"English date:{english_date.strftime('%Y-%m-%d')}")

            else:
             print("english_date") 

    elif choice=="3":
       print("Exiting. GoodBye!") 
       break
    else:
       print("Invalid Choice!.Please choose a Correct Options:")
       
      #ask a user to perform the another action or not
    print("Do You Want to perform another conversion?.")
    print("Press 'n/N' for no and any key for yes:")
    conversion_again=input()
    if(conversion_again.lower())== 'n':
       print("Exiting the Program. Good Bye!")
       break
    
    
      


if __name__ == "__main__":
 main()