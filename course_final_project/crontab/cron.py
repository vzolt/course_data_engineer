# -*- coding: utf-8 -*-

#!pip install python-crontab
from crontab import CronTab

cron = CronTab(user= True)

job = cron.new(command='python ../src/add.csv')

job.hour.every(24)
cron.write()