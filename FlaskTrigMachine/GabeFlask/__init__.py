from flask import Flask
app = Flask(__name__)

import GabeFlask.views
#app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')