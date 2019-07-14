from project import create_app
import os

conf = os.getenv('APP_ENV')

app = create_app(conf)
