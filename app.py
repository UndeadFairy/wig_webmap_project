from flask import Flask, render_template
import os
#template_dir = os.path.abspath('../static/dist')
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/lesson_page')
def lesson():
    return render_template('lesson.html')

if __name__ == '__main__':
    app.run()