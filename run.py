'''Run the app with Bjoern
This is for local development only.
'''
import bjoern

from comics.webapp.api import app

bjoern.run(app, app.config['APP_HOST'], app.config['APP_PORT'])
