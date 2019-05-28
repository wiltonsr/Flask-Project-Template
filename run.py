from project import create_app
import os

conf = os.getenv('FLASK_ENV')

app = create_app(conf)
