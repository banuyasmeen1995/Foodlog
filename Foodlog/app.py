# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 11:54:06 2022

@author: banu   
"""


from flask import Flask, render_template,request,url_for,redirect,flash
import random
import urllib.request
import os
from werkzeug.utils import secure_filename

app = Flask(__name__) 
UPLOAD_FOLDER="C:/Users/banu/Downloads/Foodlog/static/uploads"

     
app.secret_key= "secret_key"
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH']=16 *1024*1024

ALLOWED_EXTENSIONS=set(['png','jpg','jpeg','gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/' )
def home():
    return render_template('index.html')
@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file=request.files['file']
    if file.filename =='':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
        a=random.randint(50,500)
        message = "message {} message continues".format(a)  # Using the format method
        message = f"message {a} message continues"  # Using f-strings (Python >= 3.6)
        message = "message %d message continues" % (a)  # % Formatting
        message = "This Food has " + str(a) + " calories"  # Concatenation
        flash(message)
        return render_template('index.html', filename=filename)
        
    flash('Allowed image type are -png, jpg, jpeg, gif')
    return redirect(request.url)

if __name__ == '__main__':
    app.run()
