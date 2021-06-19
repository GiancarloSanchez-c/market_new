from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, EqualTo
from wtforms.fields.html5 import EmailField, IntegerField

class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired('Este campo es requerido')])
    password = PasswordField('Contraseña', validators=[DataRequired('Este campo es requerido')])
    submit = SubmitField('Ingresar')


class RegisterForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired('Este campo es requerido')])
    address = StringField('Direccion', validators=[DataRequired('Este campo es requerido')])
    name = StringField('Nombres',validators=[DataRequired('Este campo es requerido')])
    document = IntegerField ('DNI', validators=[DataRequired('Este campo es requer')])
    password = PasswordField('Contraseña', validators=[
                            DataRequired('Este campo es requerido'),
                            EqualTo('password_confirm', message='Las contraseñas no son iguales')
                        ])
    password_confirm = PasswordField('Confirmar Contraseña', 
                            validators=[DataRequired('Este campo es requerido')])
    submit = SubmitField('Registrar')