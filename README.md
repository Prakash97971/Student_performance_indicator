## Student Performance Indicator - End-to-End ML Pipeline

A machine learning application designed to predict a student's math score based on various input features like gender, ethnicity, parental education, reading and writing scores.

## Overview

Student Exam Performance Predictor is an end-to-end project that demonstrates a complete machine learning lifecycle. It handles everything from data ingestion, preprocessing, model training with hyperparameter tuning, evaluation. The final model is exposed via both Flask and Streamlit interfaces for public interaction.

- Custom data pipelines and feature engineering
- Model selection from multiple regressors with evaluation
- Trained model deployment using Flask 
- Logging and exception tracking integrated

## What the Project Does

- Allows students or educational institutions to predict expected math scores
- Provides a web interface for users to input student details and view pedictions
r
## Who It Is For

- Educators and institutions looking to estimate student performance
- Data science learners practicing full ML pipelines
- Anyone interested in regression models with real-world datasets

## Why It Is Useful

- Helps understand how academic and demographic features impact performance
- Serves as a deployable ML solution for use in real environments
- Demonstrates an industry-style ML pipeline with modular structure

## Tech Stack

- Frontend: HTML (Flask) / Streamlit
- Backend: Python, Flask
- Machine Learning: scikit-learn, pandas, numpy
- Model Training: Random Forest, XGBoost, CatBoost, Gradient Boosting, etc.
- Styling: Tailwind CSS 
- Logging: Python logging module
- Deployment: Flask server

## Installation and Setup

1. Clone the repository

```
git clone https://github.com/your-username/Student_performance_indicator.git
```

2. Create and activate a virtual environment

```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. Install dependencies

```
pip install -r requirements.txt
```

## Running the Application

### Train the Model

```
python src/components/data_ingestion.py
python src/components/data_transformation.py
python src/components/model_trainer.py
```

This will save the model and preprocessor to the `artifacts/` directory.

### Run the Flask App

```
python app.py
```

- Open browser and visit: `http://localhost:5000`
- Fill out the form and get the predicted math score

### Run the Streamlit App (Optional)

```
streamlit run streamlit_app.py
```

## Sample Input Features

- gender: Male / Female
- race_ethnicity: Group A–E
- parental_level_of_education: High School, Bachelor's, Master's, etc.
- lunch: Standard / Free-Reduced
- test_preparation_course: Completed / None
- reading_score: Integer (0–100)
- writing_score: Integer (0–100)

## Evaluation Metric

- R² Score (`sklearn.metrics.r2_score`)
- Model is saved only if the test R² is greater than 0.6


## GitHub Repository

https://github.com/Prakash97971/Student_performance_indicator.git

## Developed By

Prakash Shaw  
[GitHub Profile](https://github.com/Prakash97971)