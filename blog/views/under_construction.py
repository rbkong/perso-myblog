from  blog import app
from flask import render_template


@app.route('/')
def under_construct():
    return render_template('under_construction.html')