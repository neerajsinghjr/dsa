import os
import gzip
import shutil
from datetime import date, timedelta, datetime

# To find yesterday's date
yesterday = date.today() - timedelta(days=1)
yesterday_str = yesterday.strftime("%Y-%m-%d")

# Filenames and Directory path
#log_dir = os.getcwd()
log_dir = r'/var/log/13_karat'
filename = r'13_karat_app.log'
logfile = yesterday_str+"_"+filename
err_logfile = r'13karat_logfile_error.log'

try:
    # gzip the log file
    with open(os.path.join(log_dir, filename), 'rb') as f_in:
        with gzip.open(os.path.join(log_dir, logfile)+'.gz', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    # Empty the contents of the original log file
    open(os.path.join(log_dir, filename),'w').close()

except Exception as e:
    # Directing any error occurred to the error log file
    with open(os.path.join(log_dir, err_logfile), 'a') as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S")+' : Zipping action failed with below error:\n'+str(e))
        f.write('\n-----------------------------------------------------\n')

