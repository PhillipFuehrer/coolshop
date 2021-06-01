#region Basic Informations

#pip install holidays

"""
Customers often like to know when their orders are delivered, so we want to calculate an expected delivery date.

We deliver orders within 1-2 work days in Denmark. 
If the order is placed before 15:00 (danish time) on a work day the customer can expect the package the following work day. 
If the order is placed on a non work day or after 15:00 it will be delivered after 2 work days.

We are closed on Danish Public Holidays and in addition 
do not consider 5th of June (Constitution Day) and 31th of December (New Year’s Eve) as work days.

Write a function that takes a datetime representing the time the order was placed and returns an expected delivery date. 
Below is some examples of expected behaviour. Notice the use of UTC timezone.
"""
#UTC +2

#from datetime import timezone
#get_delivery_date(datetime.datetime(2021, 5, 20, 12, 51, 32, 199883, tzinfo=timezone.utc))
# 20.05 - 12:51
# 21.05
#datetime.date(2021, 5, 21)

# get_delivery_date(datetime.datetime(2021, 5, 20, 13, 3, 31, 245381, tzinfo=timezone.utc))
# 20.05 - 13:03
# 25.05
# datetime.date(2021, 5, 25)

# get_delivery_date(datetime.datetime(2020, 12, 29, 12, 15, 12, 0, tzinfo=timezone.utc))
# 29.12 - 12:15:12
# 30.12
# datetime.date(2020, 12, 30)

# get_delivery_date(datetime.datetime(2020, 12, 29, 14, 15, 12, 0, tzinfo=timezone.utc))
# 29.12 - 14:15:12
# 04.01
# datetime.date(2021, 1, 4)

#DK + 2 hours - so 15:00 here is 13:00 utc
#if current day is a working day and order before 13UTC then dev = the following work day
#if current day is a working day but order AFTER  13UTC then dev = 2 work days
#if current day is a holiday                            then dev = 2 work days

#endregion

from datetime import datetime, timedelta, timezone, date
import holidays
  
dk_holidays_List = []

def print_every_holiday(dk_holidays_List):

    for each_holiday in dk_holidays_List:
        print(type(each_holiday), each_holiday)

def create_holiday_list():

    for eachDay in holidays.Denmark(years = [2020,2021]).keys():

        dt = datetime.combine(eachDay, datetime.min.time())
        dk_holidays_List.append(dt)

    dk_holidays_List.extend([datetime(2021,12,31),datetime(2021,6,5),datetime(2020,12,31),datetime(2020,6,5)])

def find_next_work_day(current_day):

    for holiday in dk_holidays_List:

        if holiday.date() == current_day or current_day.weekday() > 4:

            next_day = current_day + timedelta(days=1)
            break

    else:
        return current_day

    return find_next_work_day(next_day)

def package_arrives(order):
  
    if order.hour < 13 and find_next_work_day(order.date()) == order.date():

        next_day = order.date() + timedelta(days=1)
        arrive_day = find_next_work_day(next_day)

    else:
        next_day = order.date() + timedelta(days=1)
        
        nextday = find_next_work_day(next_day)
        nextday1 = find_next_work_day(nextday + timedelta(days=1))
        
        arrive_day = nextday1

    yay_date = arrive_day.strftime("%d, %b %Y")
    print(f"Your order will arrive {yay_date}")
    #\nOrder init date {order}
    
create_holiday_list()

order_day1 = datetime(2021, 5, 20, 12, 51, 32, 199883, tzinfo=timezone.utc)
order_day2 = datetime(2021, 5, 20, 13, 3, 31, 245381, tzinfo=timezone.utc)
order_day3 = datetime(2020, 12, 29, 12, 15, 12, 0, tzinfo=timezone.utc)
order_day4 = datetime(2020, 12, 29, 14, 15, 12, 0, tzinfo=timezone.utc)

package_arrives(order_day1)
package_arrives(order_day2)
package_arrives(order_day3)
package_arrives(order_day4)