from flask import Flask,render_template,request
import pickle
import numpy as np
app=Flask(__name__)
model=pickle.load(open('iris.pkl','rb'))
@app.route('/')
def Home():
    return render_template('home.html')
@app.route('/predict',methods=['POST'])
def predict():
  if (request.method=='POST'):
    sepal_ln=float(request.values['SL'])
    sepal_wd=float(request.values['SW'])
    petal_ln=float(request.values['PL'])
    petal_wd=float(request.values['PW'])
    classfc=np.array([sepal_ln,sepal_wd,petal_ln,petal_wd])
    classfc=np.reshape(classfc,(-1,1))
    cf_pred=model.predict(classfc)
    return render_template('result.html',result=cf_pred)
if __name__ == '__main__':
     app.run()   
      