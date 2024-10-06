from flask import Flask, request, send_from_directory, jsonify
import os
from werkzeug.utils import secure_filename
import temp
import time

app = Flask(__name__)

# Define the upload folder
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploadfiles')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed file formats
ALLOWED_FORMATS = {'png', 'jpg', 'eml'}

# Function to check if the file is allowed
def allowed_file(filename):
    return '.' in filename and filename.split('.')[-1].lower() in ALLOWED_FORMATS

# Function to process the image
def process_image(filepath):
    return temp.resulter()

# Route for the index page
@app.route('/')
def index():
    return send_from_directory('../frontend', 'index.html')

# Route for file upload
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'Incorrect format'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        print("Got here")

        # Process the image and return the result
        result = process_image(file_path)
        return send_from_directory('../frontend', 'analyze.html')
    return jsonify({'error': 'File type not allowed'}), 400

@app.route('/getRes', methods=['POST'])

@app.route('/uploadfiles/<filename>', methods=['GET'])
def list_files(filename):
    result = 'bazinga' + filename
    return jsonify({'result':result})
    return send_from_directory('uploadfiles', filename)


@app.route('/result/<filename>')
def runPy():
    return jsonify({'result':'bazinga'})


@app.route('/<path:filename>')
def static_files(filename):
    time.sleep(1)

    return send_from_directory('../frontend', filename)


#@app.route('/result')
#def res_page():



# Start the Flask server
if __name__ == '__main__':
    app.run(debug=True, port=8080)
