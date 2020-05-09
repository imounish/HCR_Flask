import os
from flask import Flask, render_template, request

from core import infer

SAVE_FOLDER = os.path.abspath("../hcr_flask/static/data/")

ALLOWED_EXTENSIONS = set(['png'])

app = Flask(__name__)

def allowed_File(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/home", methods=['GET', 'POST'])
def upload_page():
    TESTFILE = "/test.png"
    if request.method == 'POST':
        # check if there is a file in the request
        if 'file' not in request.files:
            return render_template('upload.html', msg="NO File selected")
        file = request.files['file']
        # if no file is selected
        if file.filename == '':
            return render_template('upload.html', msg='No File selected')

        if file and allowed_File(file.filename):
            print(SAVE_FOLDER)
            print(SAVE_FOLDER + TESTFILE)
            file.save(os.path.abspath(SAVE_FOLDER + TESTFILE))

            # call the infer function 
            extracted_text = infer.infer(SAVE_FOLDER + TESTFILE)
            
            # extact the text and displaying it
            return render_template('upload.html', msg='Succesfully Processed', extracted_text = extracted_text, img_src = SAVE_FOLDER + TESTFILE)
        
    elif request.method == 'GET':
        return render_template('upload.html')

if __name__ == "__main__":
    app.run(debug = True)

