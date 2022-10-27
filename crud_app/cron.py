from django_cron import CronJobBase, Schedule

def MyCronJob():
    # RUN_EVERY_MINS = 1 # every 2 hours

    # schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    # code = 'crud_app.my_cron_job'    # a unique code

    # def do(self):
    print('working')
