import string
from flask import Flask, request, render_template, jsonify
from flask_cors import cross_origin
from markupsafe import Markup
import app1 as sm
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
@cross_origin()
def predict():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == "POST":
        data=str(request.form['search'])
        prediction =sm.predict(data)
        return render_template('predi.html', prediction_text=prediction)
    return render_template("index.html")
if __name__ == "__main__":
    sm.load_saved_attributes()
    app.run(debug = True)