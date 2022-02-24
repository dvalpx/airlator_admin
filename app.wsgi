#app.wsgi
import sys
sys.path.insert(0, '/var/www/html/airsim')

from app import app as application