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
