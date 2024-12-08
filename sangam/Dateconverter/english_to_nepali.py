#to convert the date from ad to ad
import datetime as dt
import nepali_datetime as ndt

def english_to_nepali(ad_year,ad_month,ad_day):
    
    try:
     #creating the object for the ad date
     ad_date=dt.date(ad_year,ad_month,ad_day)
     #converting to the nepali date
     bs_date=ndt.date.from_datetime_date(ad_date)
     return bs_date
   
    except ValueError as e:
      return f"Invalid Nepali date: {e}"

