# import streamlit as st
# from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# st.set_page_config(page_title="Student Exam Performance Predictor", layout="centered")

# st.markdown("# Student Exam Performance Indicator")
# st.markdown("### Predict Your Maths Score")

# # Collect user input
# gender = st.selectbox("Gender", ["Male", "Female"])
# ethnicity = st.selectbox("Race/Ethnicity", ["Group A", "Group B", "Group C", "Group D", "Group E"])
# parental_education = st.selectbox(
#     "Parental Level of Education",
#     ["Some High School", "High School", "Some College", "Associate's Degree", "Bachelor's Degree", "Master's Degree"]
# )
# lunch = st.selectbox("Lunch Type", ["Standard", "Free/Reduced"])
# prep_course = st.selectbox("Test Preparation Course", ["None", "Completed"])
# reading_score = st.number_input("Reading Score", min_value=0, max_value=100, step=1)
# writing_score = st.number_input("Writing Score", min_value=0, max_value=100, step=1)

# # Prediction
# if st.button("Predict Maths Score"):
#     try:
#         data = CustomData(
#             gender=gender.lower(),
#             race_ethnicity=ethnicity.lower(),
#             parental_level_of_education=parental_education.lower(),
#             lunch=lunch.lower(),
#             test_preparation_course=prep_course.lower(),
#             reading_score=reading_score,
#             writing_score=writing_score
#         )
#         pred_df = data.get_data_as_data_frame()
#         pipeline = PredictPipeline()
#         prediction = pipeline.predict(pred_df)

#         st.success(f"🎯 Predicted Maths Score: {prediction[0]:.2f}")

#     except Exception as e:
#         st.error(f"⚠️ An error occurred: {str(e)}")



from flask import Flask, request, render_template
import logging

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app= application
app.logger.setLevel(logging.DEBUG)

@app.route('/', methods=['GET'])
def index():
    # Show the same form template
    return render_template('home.html')

@app.route('/predictdata', methods=['POST'])
def predict_datapoint():
    try:
        # Log the incoming form so we can inspect it
        app.logger.debug("Form data: %s", request.form)

        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            # swap these to match your input names
            reading_score=float(request.form.get('reading_score')),
            writing_score=float(request.form.get('writing_score'))
        )

        pred_df = data.get_data_as_data_frame()
        app.logger.debug("Prepared DataFrame:\n%s", pred_df)

        pipeline = PredictPipeline()
        prediction = pipeline.predict(pred_df)
        app.logger.debug("Model output: %s", prediction)

        # Render the same form template, passing the result
        return render_template('home.html', results=prediction[0])

    except Exception as e:
        app.logger.exception("Error during prediction")
        # You can show a friendly message or re‑raise to get the full traceback in browser
        raise

if __name__ == "__main__":
    # debug=True gives you an interactive traceback page on error
    app.run(host="0.0.0.0", port=5000, debug=True)
