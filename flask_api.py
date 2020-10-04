
from flask import Flask, flash, request, redirect
from werkzeug.utils import secure_filename

app = Flask(__name__)


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
def allowed_image(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods = ['GET','POST'])
def handle_request():
    if request.method == 'POST':
        # check if the post request has the image 
        if 'image' not in request.files:
            flash('No image part')
            return redirect('/')

        imagefile = app.request.files['image']
        # if user does not select image, browser also
        # submit a empty part without filename
        if imagefile.filename == '':
            flash('No selected image')
            return redirect('/')
        if imagefile and allowed_file(imagefile.filename):
            filename = werkzeug.utils.secure_filename(imagefile.filename)
            print("\nReceived image File name : " + imagefile.filename)
            imagefile.save(filename)
            flash('successful')
            return 'Image Uploaded'
    return 'Image Uploaded Successfully'   
    
if __name__ == "__main__":
    app.run(debug=True)

        
      
       
        