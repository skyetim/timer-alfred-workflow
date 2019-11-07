# timer-alfred-workflow
A simple timer that uses Alfred native notifications. 

## Installation
- Download [Timer.alfredworkflow](https://github.com/skyetim/timer-alfred-workflow/blob/master/Timer.alfredworkflow?raw=true)
- Click to install. 

## Usage
- The general syntax is `timer [hours:minutes:seconds] [optional:title]`
- `timer 5` sets a countdown timer that goes off after 5 minutes.
- `timer 5:00` or `timer 5:` sets a timer that goes off after 5 hours.
- `timer 0:0:30` or `timer ::30` sets a timer that goes off after 30 seconds. 
- `timer 40 Laundry is done!` adds an optional title to the timer.

## TODO
- [ ] add help page
- [ ] handle exception


## Meta
This workflow is inspired by [Daniel Bader's countdown timer](https://github.com/dbader/alfred-countdown-timer). However, its notification system is based on `objc` package in Python that is no longer compatible with the new macOS Catalina. This is the reason why I started to work on this new workflow. 
