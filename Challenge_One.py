#defining a function that convers 12-hour time to 24-hour time
def time_Conversion(time):

    #checks if the time is exactly midnight(12:00:00AM) then converts it to 00:00:00
    if time[-2:] == 'AM' or time[-2:] == 'am' or time[-2:] =='Am' and time[:2] == '12':
        return '00' + time[2: -2]
    
    #checks if the time is before noon then removes the AM and keeps the time as it is
    elif time[-2:] == 'AM' or time[-2:] == 'am' or time[-2:] == 'Am':
        return time[:-2]
    
    #checks if the time is exactly midday and converts it to 12:00:00
    elif time[-2:] == 'PM'or time[-2:] == 'pm' or time[-2:] =='Pm' and time [:2] == '12':
        return time[:-2]
    
    #this checks for all other times past midday and converts them to 24-hour format by adding 12.
    else:
        return str(int(time[:2]) + 12) + time[2:8]
    
time = input()
print(time_Conversion(time))