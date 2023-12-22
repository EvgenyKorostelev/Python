from flask import Flask, render_template
from register import RegisterForm
from authorization import AuthorizationForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "KBRAI BRAINS GEEK GEENS" 

@app.route("/")
def index():
    return render_template('index.html', title='Главная страница')


@app.route("/students", methods=["GET"])
def info():
    list_std = ['Олег Антончик', 'Наталья Василенко',
                'Maria Andreeva',
                'Алексей Виноградов',
                'Антон Панфилов',
                'Евгений Коростелев',
                'Михаил Кудрявцев']
    return render_template('list_students.html', s=list_std,
                           title='Онлайн')


@app.route("/registration", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print(form.data) # dictionary
        print(form.data['name'], form.data['mail'])
    return render_template("register.html", form=form)


@app.route("/authorization", methods=["GET", "POST"])
def authorization():
    form = AuthorizationForm()
    if form.validate_on_submit():
        print(form.data) # dictionary(словарь)
        print(form.data['mail'], form.data['password'])
    return render_template("authorization.html", form=form)



if __name__ == '__main__':
    app.run()
