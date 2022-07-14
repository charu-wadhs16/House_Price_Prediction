from flask import Flask, request, render_template, jsonify
from flask_cors import cross_origin
from markupsafe import Markup
import houseprediction as tm
app = Flask(__name__)
@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': tm.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route("/")
@cross_origin()
def home():
    return render_template("myfront.html")
@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == 'GET':
        return render_template('home.html')
    if request.method == "POST":
        sqft = float(request.form['sqft'])
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])
        loc = request.form.get('loc')
        prediction = round(float(tm.predict_house_price(loc, sqft, bhk, bath)),2)
        value=Markup("BHK : {} <br><br> SQFT. : {} <br><br> BATHROOMS : {} <br><br> LOCATION : {} <br><br> COST : {} LAKHS".format(bhk,sqft,bath,loc,prediction))
        return render_template('prediction.html', prediction_text=value)
    return render_template("home.html")
@app.route("/about")
def about():
    return render_template("about.html")
if __name__ == "__main__":
    tm.load_saved_attributes()
    app.run(debug = True)