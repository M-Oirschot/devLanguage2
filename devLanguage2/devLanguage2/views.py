"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, jsonify, session
from devLanguage2 import app

@app.route('/')
@app.route('/home')
def home():
   if 'results' in session:
       results = session['results']
   else:
       session['results'] = [0,0,0] #right answers, wrong, total assignments done
       results = [0,0,0]

   return render_template(
        'index.html',
        title='Home Page'
    )

@app.route('/beginners_module')
def beginners_module():
    data = []
    return render_template(
        'module1.html',
        title='Present perfect continuous (beginner)', data=data
    )

@app.route('/beginners_module', methods=['POST'])
def getFormData():
    session['lastAssignment'] = [0,0]
    moduleAnswers = ['have been working', 'have you been doing', 'have been driving', 'has been planning','has been telling','have you been doing','have been writing','has been feeling']
    userAnswers = []
    gg = []
    x = 0
    for w in range(1, 9):
        tmp = request.form[str(w)]
        userAnswers.extend([tmp.lower()])

    for answer in moduleAnswers:
         if(answer == userAnswers[x]):
            session['results'][0] += 1
            session['lastAssignment'][0] += 1
            gg.extend(['Correct'])
         else:
             session['results'][1] += 1
             session['lastAssignment'][1] += 1
             questionAnswer = moduleAnswers[x]
             gg.extend(['Wrong, you guessed "'+userAnswers[x]+'" but the correct answer is: ' + questionAnswer])
         x+=1
    session['results'][2] += 1
    return render_template('module1.html', title='Present perfect continuous (beginner)', data=gg)

@app.route('/intermediate_module')
def intermediate_module():
    formData = []
    return render_template(
        'module2.html',
        title='Present perfect Progressive (intermediate)', frm=formData
    )

@app.route('/intermediate_module', methods=['POST'])
def getData():
    session['lastAssignment'] = [0,0]
    moduleAnswers = ['has been working', 'have been waiting', 'has been living', 'has been playing','have you been learning','have been looking for','have been living','has not been running']
    userAnswers = []
    gg = []
    x = 0
    for w in range(1, 9):
        tmp = request.form[str(w)]
        userAnswers.extend([tmp.lower()])

    for answer in moduleAnswers:
         if(answer == userAnswers[x]):
            session['results'][0] += 1
            session['lastAssignment'][0] += 1
            gg.extend(['Correct'])
         else:
             session['results'][1] += 1
             session['lastAssignment'][1] += 1
             questionAnswer = moduleAnswers[x]
             gg.extend(['Wrong, you guessed "'+userAnswers[x]+'" but the correct answer is: ' + questionAnswer])
         x+=1
    session['results'][2] += 1
    return render_template('module1.html', title='Present perfect continuous (beginner)', data=gg)


@app.route('/results')
def results():
    if 'results' not in session:
        session['results'] = [0,0,0]
    if 'lastAssignment' not in session:
        session['lastAssignment'] = [0,0]

    return render_template(
        'results.html',
        lastExercise=session['lastAssignment'],
        results=session['results'],
    )
