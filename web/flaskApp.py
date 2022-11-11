from flask import Flask, request, current_app

class MyApp(Flask):
  def __init__(self):
    Flask.__init__(self, __name__)

  def register_blueprint(self, bp):
    Flask.register_blueprint(self, bp)