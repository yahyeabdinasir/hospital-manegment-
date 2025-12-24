
from datetime  import datetime,date,timedelta
from xxlimited_35 import Null

from dateutil.relativedelta import relativedelta
# my_time = datetime.today().ctime()
# print(my_time)
#
# today = date(2025,12,20)
# new_date = today + relativedelta(month=1)
#
# print(today)
# print(new_date)
#
#
# print(datetime)
# print(date)
#
# taarikh =  relativedelta(years=1 , month=1)
# print(taarikh)
#
#



# today = date.today()
# date_of_birth = date(2002,10,1)
# # age =    date.today().year  - date_of_birth.year
# print(today)
# print(age)
# compute_date_of_bith = None
#
# if age :
#     compute_date_of_bith = today - relativedelta(years=age)
#     print("this is the compute date of birth",compute_date_of_bith)
#

#

def compute_age(DOB):
    today = date(2025,11,20)
    print(today)
    age = today.year - DOB.year
    # if today.month < DOB.month:
    #     age -=1
    # elif today.month == DOB.month and today.day < DOB.day:
    #     age -=1
    if (today.month ,today.day) < (DOB.month ,DOB.day):
        age -=1


    return age
my_compute =  date(2000,11,20)
print(compute_age(my_compute))

def inverse_age(age , month, days):
    today = date.today()
    print(today)
    DOB = today - relativedelta(years=age , months=month , days=days)
    return DOB
# my_compute =  date(25,1,3)
print( 'this is the inverse age of dob', inverse_age(15,1,3))

