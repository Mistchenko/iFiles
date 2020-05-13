import os
import pwd
import grp
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from datetime import date

uid = pwd.getpwnam("nobody").pw_uid
gid = grp.getgrnam("nogroup").gr_gid

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')
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
            os.chmod(dir, 0o777)
            os.chown(dir, uid, gid)
            full_path = os.path.join(dir, filename)
            f.save(full_path)
            os.chmod(full_path, 0o666)
            os.chown(full_path, uid, gid)
            up_files.append(filename)
            print('save:', filename)

    return render_template('index.html', up_files=up_files)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
