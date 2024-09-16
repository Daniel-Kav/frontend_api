from datetime import datetime

now = datetime.now()

print("Local Date: ", now.strftime("%Y-%m-%d"))
print("Local Time: ", now.strftime("%H:%M:%S"))
print("Local Year: ", now.year)
