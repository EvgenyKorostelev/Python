from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    # dsvsfvd
    return render_template('index.html', title='Главная страница')


@app.route("/students")
def info():
    list_std = ['Олег Антончик', 'Наталья Василенко',
                'Maria Andreeva',
                'Алексей Виноградов',
                'Антон Панфилов',
                'Евгений Коростелев',
                'Михаил Кудрявцев']
    return render_template('list_students.html', s=list_std,
                           title='Онлайн')


if __name__ == '__main__':
    app.run()