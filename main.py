with open("_chat.txt", 'r') as fp:
    text = fp.readlines()
    lines = len(text)
    pollcount = 0
    leave_events = {}
    
    for eachline in text:
        if 'POLL' in eachline:
            pollcount += 1
        elif 'left the group' in eachline:
            # Assuming the date is at the beginning of each line in a consistent format
            date = eachline.split()[0]
            if date in leave_events:
                leave_events[date] += 1
            else:
                leave_events[date] = 1
    
    print('Total Number of lines:', lines)
    print('Total polls:', pollcount)
    
    # Find the date with the most leave events
    if leave_events:
        max_leave_date = max(leave_events, key=leave_events.get)
        print('Date with the most leave events:', max_leave_date)
        print('Number of leave events on that date:', leave_events[max_leave_date])
    else:
        print('No leave events found in the chat.')
