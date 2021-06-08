# app.py
import os, json
from flask import Flask, request, abort, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = 'image-upload'

# defining a route
@app.route("/", methods=['GET']) 
def index(): 
    # returning a response
    mydata = [
        { "name": "gunawan", "age": 23 },
        {"name": "hafet", "age": 23}
    ]

    return json.dumps(mydata)

@app.route('/predict', methods=['POST'])
def make_prediction():
  if request.method=='POST':
    file_upload = request.files['image']

    if not file_upload: return json.dumps({"status": "No image is detect"})
    
    filename = secure_filename(file_upload.filename)
    if filename != '':
      file_ext = os.path.splitext(filename)[1]
      if file_ext not in app.config['UPLOAD_EXTENSIONS']:
        abort(400)
      file_upload.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    
    return json.dumps({"status": "Ok"})

@app.route("/image-upload/<path:path>")
def static_dir(path):
    # return 'Subpath %s' % escape(path)
    return send_from_directory("image-upload", path)

if __name__ == '__main__':
    # app.run()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
