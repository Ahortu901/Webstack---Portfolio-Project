"from src import create_app"
import os
from flask import Flask, render_template
from flask import url_for

app= Flask(__name__)

@app.route('/',strict_slashes=False, methods=['GET', 'POST'])
def index():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)