from datetime import datetime, timedelta

DATE_FORMAT = '%d-%m-%Y'

date_string = input('Give a date: ')


dd = datetime.strptime(date_string, DATE_FORMAT)

print(dd)

print(f"That's {dd.strftime('%Y-%m-%d')}")

now = datetime.now()
print(f"Now it's {now.strftime('%Y-%m-%d')}")

delta = now - dd

print(delta)


