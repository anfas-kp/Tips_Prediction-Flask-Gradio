import gradio as gd
import numpy as np
import pickle
import pandas as pd

# Load the model once
model = pickle.load(open('tips_model.pkl', 'rb'))

def prediction(total_bill, time, size):
    # Create DataFrame with appropriate columns
    input_data = pd.DataFrame({
        'total_bill': [total_bill],
        'time': [0 if time == 'Lunch' else 1],
        'size': [size]
    })

    # Make the prediction
    predicted = model.predict(input_data)
    
    return f'You Got ${predicted[0]:.2f} Amount As Tips'

# Gradio Interface
iface = gd.Interface(
    fn=prediction,
    inputs=[
        gd.Number(label="Enter Total Bill"),
        gd.Radio(label="Select Time", choices=['Lunch', 'Dinner']),
        gd.Number(label="Enter Party Size", minimum=1, maximum=6)
    ],
    outputs=gd.Textbox(label="Predicted Tip"),
    title="Tip Prediction",
    description="Enter the total bill, time of day, and party size to predict the tip amount."
)

iface.launch()
