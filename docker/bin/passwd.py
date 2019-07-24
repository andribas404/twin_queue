import os
from notebook.auth import passwd
passwd = passwd(os.environ.get('NOTEBOOK_PASSWORD', ''))
passwd = "c.NotebookApp.password = u'{passwd}'".format(passwd=passwd)
print(passwd)
