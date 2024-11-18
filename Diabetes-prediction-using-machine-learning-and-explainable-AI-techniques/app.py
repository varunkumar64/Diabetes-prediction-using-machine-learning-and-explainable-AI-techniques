import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import streamlit as st

data=pd.read_csv('diabetes.csv')
X=data.iloc[:,:-1].values
Y=data.iloc[:,-1].values
# numeric_data = [float(x) for x in data]

classifier=KNeighborsClassifier()
classifier.fit(X,Y)

Y_pred=classifier.predict(X)

st.header('Please enter the following information:')

pregnancies=st.text_input('Enter Pregnancies')
glucose=st.text_input('Enter Glucose')
bloodPressure=st.text_input('Enter BloodPressure')
skinThickness=st.text_input('Enter Skin Thickness')
insulin=st.text_input('Enter Insulin')
bmi=st.text_input('Enter BMI')
dpf=st.text_input('Enter Diabetics Pedigree Function')
age=st.text_input('Enter Age')

if st.button('Result'):
    # inputData=[[pregnancies,glucose,bloodPressure,skinThickness,insulin,bmi,dpf,age]]
    inputData = [[float(pregnancies), float(glucose), float(bloodPressure), float(skinThickness),
                  float(insulin), float(bmi), float(dpf), float(age)]]



    if(classifier.predict(inputData)[0]==0):
        st.success('Negative')
    else:
        st.warning('Positive')