# -*- coding: utf-8 -*-

#!pip install python-crontab
from crontab import CronTab

cron = CronTab(user= True)

job1 = cron.new(command='python ../src/add.py')
job1.day.on(0, 1, 2, 3, 4, 5, 6)

job2 = cron.new(command='python ../src/transform.py')
job2.day.on(0, 1, 2, 3, 4, 5, 6)

job3 = cron.new(command='python ../src/count.py')
job3.day.on(0, 1, 2, 3, 4, 5, 6)

cron.write()