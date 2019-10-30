from app.main import main
from flask import render_template

@main.route('/')
def index():
    return '<h1>Test</h1>'
