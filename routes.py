from flask import render_template, request
from app import analysis, feedback

@app.route('/')
def index():
    return render_template('submit.html')

@app.route('/submit', methods=['POST'])
def submit_code():
    code = request.form['code']
    analysis_results = analysis.analyze_code(code)
    feedback_results = feedback.generate_feedback(analysis_results)
    return render_template('feedback.html', feedback=feedback_results)