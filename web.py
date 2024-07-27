from flask import Flask, request, render_template, jsonify
import joblib

app = Flask(__name__)
kmeans_model = joblib.load("./models/kmeans_model")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/project")
def project():
    return render_template("project.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        try:
            # Parse input values from the form
            nitrogen = int(request.form["nitrogen"])
            phosphorous = int(request.form["phosphorous"])
            potassium = int(request.form["potassium"])
            temperature = int(request.form["temperature"])
            humidity = int(request.form["humidity"])
            ph = float(request.form["ph"])
            rainfall = int(request.form["rainfall"])

            # Prepare the data for prediction
            data = [[nitrogen, phosphorous, potassium, temperature, humidity, ph, rainfall]]
            
            # Make prediction using the loaded model
            prediction = str(kmeans_model.predict(data)[0])
            print("prediction", prediction)

            # Return prediction result as JSON
            return jsonify({"prediction": prediction})
        
        except ValueError as ve:
            # Return error message for invalid data types
            return jsonify({"error": "Invalid input: All fields must be numbers."}), 400
        
        except Exception as e:
            # Return error message for other exceptions
            return jsonify({"error": str(e)}), 500
    
    # Render a form or a relevant page if request is GET
    return render_template("predict_form.html")  # Ensure this template exists

if __name__ == "__main__":
    app.run(debug=True)
