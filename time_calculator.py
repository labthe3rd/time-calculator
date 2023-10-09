def add_time(start, duration, day=""):
    day = day.title()
    #Display start and duration to help with troubleshooting
    print("Start Time: ", start, "     Duration: ",duration,"     ",day)
    
    #First write a four loop to determine the spot where the hour and minute split
    def colon_position(time):
        for count,x in enumerate(time):
            if x == ":":
                return count
    
    
    
    col1_pos = colon_position(start)
    col2_pos = colon_position(duration)

    start_hour = start[0:col1_pos]
    start_minute = start[col1_pos+1:col1_pos+3]
    start_meridiem = start[col1_pos+4:col1_pos+6]

    duration_hour = duration[0:col2_pos]
    duration_minute = duration[col2_pos+1:col2_pos+3]

    
    #Add the minutes to determine the hours to add to the 24 hour clock
    var_new_min_raw_int = int(start_minute) + int(duration_minute)

    #Now calculate if any hours had passed
    var_new_min_hour_int = var_new_min_raw_int//60
    var_display_min_int = var_new_min_raw_int % 60

    
    #Calculate the total hours passed and convert to a 24 hour clock
    var_new_hour_int = int(start_hour) + int(duration_hour) + var_new_min_hour_int

    #Add 12 hours to start_hour_int so we are working with 24 hour clock
    if(start_meridiem == "PM"):
        var_new_hour_int += 12

    #Now calculate the days passed if we need to
    var_total_days_passed_int = var_new_hour_int//24
    var_display_hour_int = var_new_hour_int%24
    var_display_meridiem = "AM"
    if var_display_hour_int > 12:
        var_display_hour_int = var_display_hour_int % 12
        var_display_meridiem = "PM"
    if var_display_hour_int == 12:
        var_display_meridiem = "PM"
    if var_display_hour_int == 0:
        var_display_hour_int = 12
        var_display_meridiem = "AM"
        
    #Add a leading zero if var_display_min_int is greater than 0
    if var_display_min_int >= 10:
        var_display_min = str(var_display_min_int)
    else:
        var_display_min = "0" + str(var_display_min_int)
    
    print("Total days passed: ",var_total_days_passed_int)
    new_time = str(var_display_hour_int) + ":" + var_display_min + " " + var_display_meridiem
    
    #Handle convert current day to an int so we can determine the label if it exists
    if day != "":
        if day == "Sunday":
            var_current_day_int = 1
        if day == "Monday":
            var_current_day_int = 2
        if day == "Tuesday":
            var_current_day_int = 3
        if day == "Wednesday":
            var_current_day_int = 4
        if day == "Thursday":
            var_current_day_int = 5
        if day == "Friday":
            var_current_day_int = 6
        if day == "Saturday":
            var_current_day_int = 7
        
        print("Current day as an int is ",var_current_day_int)
        var_new_day_int = (var_current_day_int + var_total_days_passed_int)%7
        print("New day int ", var_new_day_int)
        
        if var_new_day_int % 1 == 0:
            new_day = "Sunday"
        if var_new_day_int % 2 == 0:
            new_day = "Monday"
        if var_new_day_int % 3 == 0:
            new_day = "Tuesday"
        if var_new_day_int % 4 == 0:
            new_day = "Wednesday"
        if var_new_day_int % 5 == 0:
            new_day = "Thursday"
        if var_new_day_int % 6 == 0:
            new_day = "Friday"
        if var_new_day_int % 7 == 0:
            new_day = "Saturday"
        print(new_day) 
        new_time = new_time + ", " + new_day
    
    if var_total_days_passed_int == 1:
        new_time = new_time + " (next day)"
    if var_total_days_passed_int > 1:
        new_time = new_time + " (" + str(var_total_days_passed_int) + " days later)"
    print(new_time)


    return new_time