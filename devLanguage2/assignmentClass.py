from flask import session
class assignmentClass(object):
    """description of class"""
    def __init__(self,data,name,desc):
        self.data = data
        self.name = name
        self.description = desc

    def Exercise1(self):
        if request.method == 'GET':
            return render_template('module1.html')
        elif request.method == 'POST':
            givenAnswersG1 = model.Inputuser()
            rightAnswersG1 = ['have been working', 'have you been doing', 'have been driving', 'has been planning','has been telling','have you been doing','have been writing','has been feeling']
            score = model.Result()
            return render_template("module1.html", givenAnswersG1=givenAnswersG1, rightAnswersG1=rightAnswersG1, score=score)

    def Result(self):
        score = 0
        for w in range(1, 9):
            if self.givenAnswersG1[i] == self.rightAnswersG1[i]:
                session['results'][0] += 1
            else:
                session['results'][1] += 1
        return score