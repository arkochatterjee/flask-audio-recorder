from flask import Flask
from flask import request
from flask import render_template
import os

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        f = request.files['audio_data']
        with open('audio.wav', 'wb') as audio:
            f.save(audio)
        print('file uploaded successfully')
        '''

        video path = ML_model(audio.wav)
        return render_template('index.html', request="POST", 'output' : video path)

        '''

        return render_template('index.html', request="POST")
    else:
        return render_template("index.html")


def ML_model(file_location):
    a = 0
    #import all ML functions her

    #generate video
    # save video - keep name SAME
    # return video location

    #return 

if __name__ == "__main__":
    app.run(debug=True)