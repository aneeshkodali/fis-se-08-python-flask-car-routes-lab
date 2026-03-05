existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Flatiron Cars"

@app.route('/<string:model>')
def model_exists(model):
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"
    return f"No models called {model} exists in our catalog"