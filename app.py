import os
from bottle import *

@route('/')
def index():
  return "Halló Heroku!"
  
  run(hosts='0.0.0.0'), port=os.environ.get('PORT')
