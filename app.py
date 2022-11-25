
from flask import Flask,request, render_template
from function import Progression_Prediction

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def  predict():

    data = request.form
    age = float(data['age'])
    sex = float(data['sex'])
    bmi = float(data['bmi'])
    bp =float(data['bp'])
    s1 = float(data['s1'])
    s2 = float(data['s2'])
    s3 = float(data['s3'])
    s4 = float(data['s4'])
    s5 =float(data['s5'])
    s6 =float(data['s6'])

    

    Progression = Progression_Prediction(age,sex,bmi,bp,s1,s2,s3,s4,s5,s6)
    predicted_price = Progression.Predict_Progression()
    print(predicted_price)

    return render_template('index.html',Progression_Prediction=predicted_price)


if __name__ == "__main__":
    app.run(debug=True)