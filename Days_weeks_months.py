int_age=int(age)
total_weeks= int_age* 52
total_days= total_weeks * 7
total_months= int_age*12

total_weeks_left = 4680 - total_weeks
total_days_left = 32760 - total_days
total_months_left = 1080 - total_months
print(f"You have {total_days_left} days, {total_weeks_left} weeks, and {total_months_left} months left.")
