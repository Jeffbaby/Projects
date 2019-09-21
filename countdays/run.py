import datetime

d1 = datetime.datetime(2019,8,6)
d2 = datetime.datetime(2019,9,26)
interval = d2 - d1
d = interval.days
m = d*50
print("出差住宿天数为： ", (d+1))
print("出差需要开发票为：", m)