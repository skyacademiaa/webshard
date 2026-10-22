"""
WSGI configuration for PythonAnywhere.
Copy the contents of this file into your PythonAnywhere WSGI configuration file:
/var/www/<your-username>_pythonanywhere_com_wsgi.py
"""
import os
import sys

# 1. Path to your project directory
# Replace '<your-username>' with your actual PythonAnywhere username:
username = '<your-username>'
path = f'/home/{username}/Tech_Service'

if path not in sys.path:
    sys.path.append(path)

# 2. Set DJANGO_SETTINGS_MODULE
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings.development'

# 3. Serve WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
