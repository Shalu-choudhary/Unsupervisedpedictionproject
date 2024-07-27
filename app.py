from flask import Flask, request,url_for,render_template
import joblib
app=Flask(__name__)
kmeans_model = joblib.load("./models/kmeans_model")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/project")
def project():
    return render_template("project.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request=="POST":
        nitrogen=int(request.form["nitrogen"])
        phosphorous=int(request.form["phosphorous"])
        potassium=int(request.form["potassium"])
        temperature=int(request.form["temperature"])
        humidity=int(request.form["humidity"])
        ph=int(request.form["ph"])
        rainfall=int(request.form["rainfall"])
        
        data=[[nitrogen,phosphorous,potassium,temperature,humidity,ph,rainfall]]
        prediction = str(kmeans_model.predict(data)[0])
        print("prediction",prediction)
        # return prediction
        
        








if __name__=="__main__":
    app.run(debug=True)