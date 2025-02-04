import streamlit as st
import pickle
import pandas as pd

st.title('TIPS PREDICTION')
st.subheader('ENTER YOUR DATA')

total_bill=st.number_input(' Enter total_bill Amount')
time=st.selectbox('Select Time',['Lunch','Dinner'])
size=st.number_input('Enter The Size',min_value=1,max_value=6)

input_data={'total_bill':total_bill,'time':time,'size':size}

new_data=pd.DataFrame([input_data])

new_data['time']=new_data['time'].map({'Lunch':0,'Dinner':1})

df=pd.read_csv('features_tips.csv')

column_list=[col for col in df.columns if col!='Unnamed!:0']

model=pickle.load(open('tips_model.pkl','rb'))

prediction=model.predict(new_data)

if st.button('PREDICT'):
    st.write(f'You Got ${prediction[0]:2f} Amout As Tips')