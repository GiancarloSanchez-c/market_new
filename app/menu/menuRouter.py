from app import app
from flask import render_template

@app.route('/menu')
def menu():
    return render_template('menu.html')