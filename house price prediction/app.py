from flask import Flask,render_template,request
import pickle
import numpy as np
import pandas as pd
app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))
@app.route('/')
def house():
    return render_template('house(flask).html')
@app.route('/predict',methods=['post'])
def predict():
    area=float(request.values['area'])
   
    d=pd.Series(area)
    d1=pd.DataFrame(d)
    pre=model.predict(d1)
    print('your home price predictoin is:',pre)
    
    print (area)
    return render_template('house(flask).html',prediction=pre)
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(port=8000)