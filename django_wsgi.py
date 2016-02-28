import os
import sys

# ADD YOUR PROJECT TO THE PYTHONPATH FOR THE PYTHON INSTANCE
path = '/root/www/wanblog'
if path not in sys.path:
    sys.path.append(path)

        # IMPORTANTLY GO TO THE PROJECT DIR
os.chdir(path)

        # TELL DJANGO WHERE YOUR SETTINGS MODULE IS LOCATED
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wanblog.settings')

        # IMPORT THE DJANGO SETUP - NEW TO 1.7
import django
django.setup()

        # IMPORT THE DJANGO WSGI HANDLER TO TAKE CARE OF REQUESTS
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
