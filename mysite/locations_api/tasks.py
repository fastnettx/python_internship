from __future__ import absolute_import, unicode_literals

from celery.schedules import crontab
from celery.task import periodic_task
from django.core.mail import send_mail
from mysite.celery import app
from mysite import settings


@app.task()
def send_email_when_creating(user_email, country_name):
    print(user_email + country_name)
    send_mail(
        subject='Country creating',
        message='Congratulations! Your country was successfully added!',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user_email, ],
        fail_silently=False,
    )


@app.task()
def send_email_when_changing(user_email, country_name, country_id):
    print(user_email + country_name + "   :   " + str(country_id))
    send_mail(
        subject='Country ' + country_name + ' changing',
        message='Your country ' + country_name + ' was changed. You can view changes at ' +
                'http://127.0.0.1:8000/locations/list_of_counries/country' + str(country_id) + '/',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user_email, ],
        fail_silently=False,
    )


@periodic_task(run_every=(crontab(minute='*/20')), name='repeat_task')
def repeat_task():
    print('Test print to console using Celery ')
