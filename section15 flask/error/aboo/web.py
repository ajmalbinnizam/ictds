from flask import Flask,render_template,request
import pickle
import numpy as np

app=Flask(__name__)

model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    features =float (request.values['SL','SW','PL','PW'])
    features=np.reshape(features(-1,1))
    output=model.predict(features)
    output=output.item()    
    output=round(output,2)
    return render_template('result.html', prediction_text='classification of the flower is{}'.format(output))

if __name__=='__main__':
    app.run()



 