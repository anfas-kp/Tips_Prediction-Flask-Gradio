# Tips Prediction - Flask & Gradio

This project demonstrates how to build and deploy a machine learning model to predict tips using both Flask and Gradio interfaces. It includes data processing, model training, and deployment scripts.

## Project Structure

```
TIPS_PREDICTION/
|├── features_tips.csv       # Dataset with features for prediction
|├── requirements.txt        # Python dependencies
|├── tips.ipynb              # Jupyter notebook for data exploration and model building
|├── tips_gradio.py          # Gradio app for tips prediction
|├── tips_model.pkl          # Serialized machine learning model
|└── tips_site.py            # Flask web app for model deployment
```

## Installation

1. **Clone the repository:**

```bash
git clone <repository-url>
cd Tips_Prediction-Flask-Gradio-main/TIPS_PREDICTION
```

2. **Create a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install the required packages:**

```bash
pip install -r requirements.txt
```

## Usage

### 1. Run the Flask App

To deploy the tips prediction model using Flask:

```bash
python tips_site.py
```

This will start a local server, typically accessible at `http://127.0.0.1:5000/`.

### 2. Run the Gradio App

To use the Gradio interface for tips prediction:

```bash
python tips_gradio.py
```

Gradio will provide a link to interact with the model via a simple web interface.

## Dataset

The dataset `features_tips.csv` is used for training the model. It contains features relevant to predicting the tip amount, such as total bill, service quality, etc.

## Model

The machine learning model is trained and saved as `tips_model.pkl`. This model is used in both Flask and Gradio applications to make predictions.

## Contributing

Feel free to fork this repository, make enhancements, and submit pull requests.

## License

This project is licensed under the MIT License.

---

Enjoy predicting tips!

