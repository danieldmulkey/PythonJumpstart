import datetime

print('----------------------------------')
print('         BIRTHDAY APP')
print('----------------------------------')

year = int(input('What year were you born [YYYY]? '))
month = int(input('What month were you born [MM]? '))
day = int(input('What day were you born [DD]? '))

birthdate = datetime.date(year, month, day)
today = datetime.date.today()

if today - datetime.date(today.year, month, day) > datetime.timedelta(0):
    next_year = today.year + 1
else:
    next_year = today.year

next_birthday = datetime.date(next_year, month, day)
num_days = next_birthday - today

echo = 'It looks like you were born on {}'.format(birthdate.strftime('%x'))
calculate = 'Looks like your birthday is in {} days'.format(num_days.days)
comment = 'Hope you\'re looking forward to it!'

print(echo)
print(calculate)
print(comment)