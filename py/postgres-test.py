import pendulum
d1=pendulum.yesterday() #昨天
#print(d1)

d2=pendulum.today()

days=d2.diff(d1).in_days()
#print(days)
dt1=pendulum.datetime(2023,8,17)
#print(dt1.timezone.name) #UTC
dt2 = pendulum.datetime(2021, 10, 3, tz="Asia/Shanghai")
#print(dt2.timezone.name)
in_perk=pendulum.now()
print(in_perk.in_timezone("Asia/Shanghai"))
