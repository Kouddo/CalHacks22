import os
from flask import Flask, flash, request, redirect, url_for, render_template, abort, send_from_directory, send_file
from werkzeug.utils import secure_filename
from flask_dropzone import Dropzone
from logging import FileHandler,WARNING

app = Flask('__name__')
dropzone = Dropzone(app)

ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('home.html')

@app.route('/output', methods=['GET', 'POST'])
def output():
    print("REDIRECT")
    return render_template('rendertools.html')

@app.route('/tools', methods=['GET', 'POST'])
def tools():
    if request.method == 'POST':
        print('red1')
        return redirect("http://www.example.com", code=302)

        # return send_from_directory(directory='uploads', filename='demofile2.txt', as_attachment=True)
        # return send_file('./demofile2.txt', attachment_filename='thing.txt')
        # f = open("demofile2.txt", "w+")
        # f.write("TESTING")
        # f.close()
        # # check if the post request has the file part
        # if 'file' not in request.files:
        #     flash('No file part')
        #     return redirect(request.url)
        # file = request.files['file']
        # # If the user does not select a file, the browser submits an
        # # empty file without a filename.
        # if file.filename == '':
        #     flash('No selected file')
        #     return redirect(request.url)
        # if file and allowed_file(file.filename):
        #     filename = secure_filename(file.filename)
        #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #     return redirect(url_for('download_file', name=filename))
    return render_template('tools.html')


# @app.route('/', methods=['GET', 'POST'])
# def upload_file():
#     if False: # request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']
#         # If the user does not select a file, the browser submits an
#         # empty file without a filename.
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             return redirect(url_for('download_file', name=filename))
#     return render_template('testing.hmtl')

@app.route('/json-example')
def json_example():
    return 'JSON Object Example'

# if __name__ == '__main__':
#     # run app in debug mode on port 5000
#     app.run(debug=True, port=5000)
