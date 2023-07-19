from flask import Flask,render_template,request
import pickle
import numpy as np
import pandas as pd
app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))
@app.route('/')
def house():
    return render_template('salary.html')
@app.route('/predict',methods=['post'])
def predict():
    exp=int(request.values['salary'])
    print(exp)
   
    d=pd.Series(exp)
    d1=pd.DataFrame(d)
    pre=model.predict(d1)
    print('your home price predictoin is:',pre)
    
    print (exp)
    return render_template('salary.html',prediction=pre)
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(port=8000)