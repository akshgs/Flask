from flask import Flask,render_template,request
import pickle
import numpy as np
import pandas as pd
app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))
@app.route('/')
def loan():
    return render_template('loan.html')
@app.route('/predict',methods=['post'])
def predict():
    edu=int(request.values['edu'])
    print("edu",edu)
    emp=int(request.values['emp'])
    print("emp",emp)
    income=int(request.values['income'])
    print("income",income)
    amt=int(request.values['amt'])
    print("amt",amt)


    data=[[edu,emp,income,amt]]
    df=pd.DataFrame(data,columns=['Education','Self_Employed','ApplicantIncome','LoanAmount'])
    a=model.predict(df)
    print(a)
    if a==0:
        print('you are not eligible')
        x="you are not eligible"
    else:
        print('you are eligible')
        x="you are eligible"
    return render_template('loan.html',prediction=x)
if __name__=='__main__':
    app.run(port=8000)

