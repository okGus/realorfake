from app import app
from flask import render_template, request

import pickle
from skimage import io
from skimage import transform

# path_to_image_classifier = 'models/image-classifier.pkl'

# with open(path_to_image_classifier, 'rb') as f:
#     image_classifier = pickle.laod(f)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    if request.method == 'GET':
        return render_template('classify_image.html')

    if request.method == 'POST':
        # Get file object from user input.
        file = request.files['file']

        if file:
            # Read the image using skimage
            img = io.imread(file)

            # Resize the image to match the input of the model will accept
            img = transform.resize(img, (960, 960))

            # Flatten image
            img = img.flatten()

            # Get prediction of image from classifier
            predictions = image_classifier.predict([img])

            # Get the value of the prediction
            prediction = predictions[0]

            return render_template('classify_image.html', prediction=str(prediction))

        return render_template('classify_image.html')