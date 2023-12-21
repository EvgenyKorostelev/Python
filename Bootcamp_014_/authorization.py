from flask_wtf import FlaskForm
from wtforms import SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired
# flask-login

class AuthorizationForm(FlaskForm):
    mail = EmailField("Почта: ", validators=[DataRequired()])
    password = PasswordField("Пароль: ", validators=[DataRequired()])
    enter = SubmitField("Войти")
