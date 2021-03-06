from app import app
from flask import render_template, request

from werkzeug.utils import secure_filename
from keras.preprocessing import image
import numpy as np
from tensorflow.keras import models
import os

UPLOAD_FOLDER = '/home/gus/Projects/webapp/realorfake/app/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

resModel = models.load_model('app/models/resModel.h5')


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('index.html')


@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    if request.method == 'GET':
        return render_template('classify_image.html')

    if request.method == 'POST':
        # Delete content in images folder
        folder = os.path.join(app.config["UPLOAD_FOLDER"])
        images_folder = os.listdir(folder)
        if len(images_folder) > 200: # delete content of folder if images contains +200
            for i in images_folder:
                try:
                    os.remove(folder+'/'+i)
                except OSError as e:
                    print("Error: %s : %s" % (i, e.strerror))

        # Get file object from user input.
        file = request.files['file']

        if file:
            filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'],filename)
            file.save(path)

            # Read the image using keras preprocessing
            img = image.load_img(path, target_size=(256, 256, 3))

            # Resize the image to match the input of the model will accept
            img = image.img_to_array(img)

            # Rescale
            img = img / 255

            # Expand dimensions
            img = np.expand_dims(img, axis=0)

            # Get prediction of image from ResNet
            result = resModel.predict(img)[0][0]

            # Get the value of the prediction
            prediction = (result < 0.5).astype(np.int)

            # String prediction
            final_str_pred = "Fake" if prediction == 0 else "Real"

            # Confidence
            confidence = result * \
                100 if final_str_pred == "Fake" else (1 - result) * 100

            return render_template('classify_image.html', final_str_pred=final_str_pred, confidence=confidence, image_=file.filename)

        return render_template('classify_image.html')


@app.route('/uploads/<filename>')
def send_uploaded_file(filename=""):
    from flask import send_from_directory
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)