from flask import Flask, request, render_template, jsonify
import joblib
import pandas as pd 
app = Flask(__name__)
kmeans_model = joblib.load("./models/kmeans_model")
std=joblib.load('./models/standard_scaler')

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
            converted_data=std.transform(data)
            prediction=kmeans_model.predict(converted_data)[0]
            print("prediction", prediction)

            df=pd.read_csv(r'C:\Users\hp\Desktop\farmer project\models\app_data.csv')
            if prediction==0:
                cluster=df[df['cluster']==0]
                ls=list(cluster['Label'].value_counts().keys())
                return render_template('group0.html')
            elif prediction==1:
                cluster=df[df['cluster']==1]
                ls=list(cluster['Label'].value_counts().keys())
                return render_template('group1.html')
            elif prediction==2:
                cluster=df[df['cluster']==2]
                ls=list(cluster['Label'].value_counts().keys())
                return render_template('group2.html')
            elif prediction==3:
                cluster=df[df['cluster']==3]
                ls=list(cluster['Label'].value_counts().keys())
                return render_template('group3.html')
            elif prediction==4:
                cluster=df[df['cluster']==4]
                ls=list(cluster['Label'].value_counts().keys())
                return render_template('group4.html')
            elif prediction==5:
                cluster=df[df['cluster']==5]
                ls=list(cluster['Label'].value_counts().keys())
                return render_template('group5,6,7.html')
            elif prediction==6:
                cluster=df[df['cluster']==6]
                ls=list(cluster['Label'].value_counts().keys())
                return render_template('group5,6,7.html')
            elif prediction==7:
                cluster=df[df['cluster']==7]
                ls=list(cluster['Label'].value_counts().keys())
                return render_template('group5,6,7.html')
            # Return prediction result as JSON
            return jsonify({"prediction": prediction})
        
        
        except ValueError as ve:
            # Return error message for invalid data types
            return jsonify({"error": "Invalid input: All fields must be numbers."}), 400
        
        except Exception as e:
            # Return error message for other exceptions
            return jsonify({"error": str(e)}), 500
    
    

if __name__ == "__main__":
    app.run(debug=True)
