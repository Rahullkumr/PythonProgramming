import datetime

from newfile import newfile_fn
newfile_fn()


print("==========================")
print("DATETIME MODULE")
print("==========================")

x = datetime.datetime.now()
print('current date and time: ', x)
print('year in YY format: ', x.strftime("%y"))
print('year in YYYY format: ', x.strftime("%Y"))
print('month name in MMM format: ', x.strftime("%b"))
print('full month name: ', x.strftime("%B"))
print('numeric month value in MM format: ', x.strftime("%m"))
print('current hour in clock 24hr format: ', x.strftime("%H"))
print('current hour in clock 12hr format: ', x.strftime("%I"))
print('current minute in clock: ', x.strftime("%M"))
print('current time AM/PM format: ', x.strftime("%p"))
