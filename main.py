from flask import Flask, render_template, redirect, request
from data import db_session
from data.users import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/data.db")
    app.run()


@app.route('/reg', methods=['POST', 'GET'])
def reg():
    if request.method == 'GET':
        user = "Ученик Яндекс.Лицея"
        return render_template("registration.html")
    elif request.method == 'POST':
        user = User()
        user.name = request.form['name']
        user.surname = request.form['surname']
        user.email = request.form['email']
        user.sex = request.form['sex']
        db_sess = db_session.create_session()
        db_sess.add(user)
        db_sess.commit()
        return "Форма отправлена"


if __name__ == '__main__':
    main()
