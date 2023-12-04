from time import sleep
import os
import schedule


def job_login():
    os.system('python -m unittest ./Test/Login.py')


schedule.every(13).seconds.do(job_login)
# schedule.every().day.at("15:34").do(job_main)
# schedule.every(10).minutes.do(job_login)


while True:
    schedule.run_pending()
    sleep(1)


