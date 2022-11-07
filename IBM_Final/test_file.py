from datetime import datetime as dt
hour = str(dt.now()).split()[1].split(":")[0]
print(hour)
