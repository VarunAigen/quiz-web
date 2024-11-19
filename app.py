from flask import Flask, render_template, request
from questions import get_questions  # Importing questions

app = Flask(__name__)

# Fetching the list of questions from the questions.py file
questions = get_questions()

@app.route('/')
def index():
    # Render the main quiz page with the questions
    return render_template('index.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    # Check answers
    for question in questions:
        user_answer = request.form.get(str(question['id']))
        if user_answer and user_answer == question['answer']:
            score += 1
    # Render the result page after submission
    return render_template('result.html', score=score, total=len(questions))

if __name__ == '__main__':
    app.run(debug=True)
