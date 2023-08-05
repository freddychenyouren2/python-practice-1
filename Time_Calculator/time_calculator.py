def add_time(start_time, duration, start_day=None):
    #Steps 1 - 3
    start_time_wo_ampm = start_time[:-2].split(':')
    start_time_hour, start_time_min = map(int, start_time_wo_ampm)
    AM_OR_PM = start_time[-2:].upper()
    duration_hour, duration_min = map(int, duration.split(':'))

    if AM_OR_PM == "PM":
        start_time_hour += 12
    
    #Step 4
    total_hour = start_time_hour + duration_hour
    total_min = start_time_min + duration_min
    
    if total_min > 60:
        total_min -= 60
        total_hour += 1
    
    #step 5 - 8
    num_of_days_passed = total_hour // 24
    remaining_hour = total_hour % 24

    NEW_AM_OR_PM = "AM" if remaining_hour < 12 else "PM"

    if remaining_hour == 0:
        remaining_hour = 12
    elif remaining_hour > 12:
        remaining_hour -= 12
    
    #step 9
    new_time = f'{remaining_hour}:{str(total_min).zfill(2)} {NEW_AM_OR_PM}'

    #steps 10-11
    if start_day:
        all_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        start_day = start_day.lower().capitalize()
        day_index = all_days.index(start_day) #Get the position of the day
        new_day_index = (day_index + num_of_days_passed) % 7
        new_day = all_days[new_day_index]
        #Update new_time
        new_time += f', {new_day}'

    #step 12
    if num_of_days_passed == 1:
        new_time += ' (next day)'
    elif num_of_days_passed > 1:
        new_time += f' ({num_of_days_passed} days later)'
    
    #step 13
    return new_time