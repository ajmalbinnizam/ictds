from flask import Flask, render_template, request, session

app = Flask(__name__)
from Classifier import  MyClassifier
app.secret_key = 'any random string'

@app.route('/')
def student():
   return render_template('home.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      a	= request.form['sepal-length']
      b = request.form['sepal-width']
      c = request.form['petal-length']
      d = request.form['petal-width']
      inputlist=[a,b,c,d]
      ob=MyClassifier()
      result1=ob.predict(list1=inputlist)
      final_result = str(result1)
      return render_template("prediction.html", result =  final_result )

if __name__ == '__main__':
    #app.run(debug = True)
    app.run(port=5000)
    
'''if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)'''