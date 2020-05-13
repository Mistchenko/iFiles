import os
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from datetime import date

app = Flask(__name__)
app.debug = True
app.config['UPLOAD_FOLDER'] = '/store'


@app.route('/', methods=['GET', 'POST'])
def index():
    up_files = []
    if request.method == 'POST':
        # file = request.files['fls']
        #file = request.files.getlist("fls")
        #print('fls:', file)
        d = date.today()
        subdir = '{}-{}-{}'.format(d.year, d.month, d.day)
        for f in request.files.getlist("fls"):
            filename = secure_filename(f.filename)
            dir = os.path.join(app.config['UPLOAD_FOLDER'], subdir)
            os.makedirs(dir, exist_ok=True)
            f.save(os.path.join(dir, filename))
            up_files.append(filename)
            print('save:', filename)

    return render_template('index.html', up_files=up_files)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
