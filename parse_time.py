import sys
import json

argvs = sys.argv[1].split(' ')

def parse_time():
    """Parse and return the desired countdown duration in seconds from
    the commandline.
    """
    hours, minutes, seconds = '','',''
    duration = argvs[0]
    splitted_duration = duration.split(':')
    if len(splitted_duration) == 3:
        hours, minutes, seconds = splitted_duration
    elif len(splitted_duration) == 2:
        hours, minutes = splitted_duration
    else:
        minutes = splitted_duration[0]
    hours = hours if hours != '' else 0
    minutes = minutes if minutes != '' else 0
    seconds = seconds if seconds != '' else 0
    return int(hours)*3600 + int(minutes) * 60 + int(seconds)


interval = parse_time()

hours = interval // 3600

resid = interval - hours*3600
minutes = resid / 60
seconds = resid % 60
label = ' '.join(argvs[1:])

output = {
        "hours": hours, 
        "minutes": minutes, 
        "seconds": seconds, 
        "label" : label
    }


js = {"alfredworkflow": {
    "arg": interval,
    "variables": output}}

print(json.dumps(js))