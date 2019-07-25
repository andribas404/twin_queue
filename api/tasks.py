import os
import subprocess
import requests

from celery import shared_task

from django.conf import settings


TASK_FILE_PATH = 'twin/task.py'
API_START_URL = 'http://nginx/{pk}/start/'
API_COMPLETE_URL = 'http://nginx/{pk}/complete/'


@shared_task
def task_run(pk):
    url = API_START_URL.format(pk=pk)
    r = requests.post(url)
    task_file = os.path.join(settings.BASE_DIR, TASK_FILE_PATH)
    proc = subprocess.run(['python', task_file])
    url = API_COMPLETE_URL.format(pk=pk)
    r = requests.post(url)
    return proc.returncode
