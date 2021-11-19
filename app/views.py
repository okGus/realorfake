from app import app
from flask import render_template, request

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    if request.method == 'GET':
        return render_template('classify_image.html')

    if request.method == 'POST':
        return render_template('classify_image.html')