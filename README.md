# Credit Score Predictor with FastAPI

<p align="center">
  <img src="python/frontend/static/images/meter.png" alt="Credit Score Predictor Logo" style="width:500px;">
</p>


This FastAPI-based web application is designed to predict credit scores using machine learning. The project follows a systematic data preprocessing and feature selection approach to ensure the model's accuracy and efficiency.

## Project Overview

### Data Cleaning and Transformation

The project began with comprehensive data preprocessing. The dataset initially contained numerous unnecessary columns, making it crucial to streamline the information for efficient model training. To achieve this, the following steps were taken:

- **Data Cleaning**: The dataset was cleaned to remove any missing or erroneous values, ensuring that the data used for training and predictions was of high quality.

- **Feature Selection**: To identify the most relevant features for credit score prediction, a heatmap was employed to visualize the correlation between variables. Only the columns that demonstrated a significant impact on credit scores were retained for further analysis.

### Machine Learning Model

With the refined dataset, a machine learning model was developed to predict credit scores based on user-input financial parameters. The model was trained on the carefully selected features, leveraging historical data to make accurate predictions.

### FastAPI Integration

FastAPI, a modern web framework for building APIs with Python, was employed to create a user-friendly interface for credit score prediction. Users can input their financial information through a user-friendly form, and the FastAPI application processes these inputs to provide a credit score prediction.

## Key Features

- **Data Cleaning and Transformation**: The project incorporates robust data preprocessing techniques to ensure the quality of the dataset used for credit score prediction.

- **Feature Selection**: Only the most relevant features are retained for model training, enhancing prediction accuracy.

- **Machine Learning Model**: A trained machine learning model leverages historical data to predict credit scores based on user inputs.

- **FastAPI Integration**: FastAPI provides a seamless and user-friendly interface for users to input their financial data and receive credit score predictions.


## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [HTML Templates](#html-templates)
- [Dependencies](#dependencies)


## Installation

1. Clone the repository:

   ```shell
   https://github.com/Prem07a/Credit-Score-Classification.git
   cd credit-score-predictor
   ```
2. Make Vitrual Env
   ```shell
   python -m venv venv
   ```

3. Activate vitrual env
- (Windows/Linux)
   ```shell
   .\venv\Scripts\activate
   ```
- (Mac)
   ```shell
   source venv/bin/activate
   ```

4. Install Requirements
   ```shell
   pip install -r requirements.txt
   ```

5. Run the FastAPI application:

   ```shell
   uvicorn python.backend.main:app --reload
   ```


## Usage

To use this credit score predictor, follow these steps:

1. Ensure you have the required dependencies installed (see [Dependencies](#dependencies) section).
2. Clone the repository as mentioned in the installation steps.
3. Run the FastAPI application.

## Endpoints

1. **Main Form Page**
   - URL: `/`
   - HTTP Method: GET
   - Description: Renders the main form page where users can input their financial data.

2. **Credit Score Prediction**
   - URL: `/predict`
   - HTTP Method: POST
   - Description: Predicts the user's credit score based on the input data and returns a credit grade.
   - Request Parameters: (List of parameters...)

3. **Resume Page**
   - URL: `/resume`
   - HTTP Method: GET
   - Description: Renders a resume page.

4. **Hire Me Page**
   - URL: `/hire`
   - HTTP Method: GET
   - Description: Renders a "Hire Me" page.

5. **Thank You Page**
   - URL: `/thankyou`
   - HTTP Method: POST
   - Description: Saves user's contact information and message to a file and displays a "Thank You" page.
   - Request Parameters: (List of parameters...)

You can find HTML templates in the project's `templates` directory.

## Dependencies

Make sure to have the following dependencies installed:

- [FastAPI](https://fastapi.tiangolo.com/)
- [uvicorn](https://www.uvicorn.org/)
- [pandas](https://pandas.pydata.org/)
- [joblib](https://joblib.readthedocs.io/en/latest/)
- [Jinja2](https://jinja.palletsprojects.com/en/3.0.x/)
- [Sklearn](https://scikit-learn.org/stable/)
