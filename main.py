# app.py
from flask import Flask, render_template, request
import os, json

UPLOAD_FOLDER = '/image-upload'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# defining a route
@app.route("/", methods=['GET']) 
def index(): 
    # returning a response
    mydata = {"name": "gunawan", "age": 23}

    return json.dumps(mydata)

@app.route('/predict', methods=['POST'])
def make_prediction():
  if request.method=='POST':
    # get uploaded image file if it exists
    file = request.files['image']
    if not file: return json.dumps({"status": "No image is detect"})
    
    # read in file as raw pixels values
    # (ignore extra alpha channel and reshape as its a single image)
    
    # img = misc.imread(file)
    # img = img[:,:,:3]
    # img = img.reshape(1, -1)

    # make prediction on new image
    # prediction = model.predict(img)

    # squeeze value from 1D array and convert to string for clean return
    # label = str(np.squeeze(prediction))

    # switch for case where label=10 and number=0
    # if label=='10': label='0'
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

    return json.dumps({"status": "ok"})

if __name__ == '__main__':
    # app.run()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
