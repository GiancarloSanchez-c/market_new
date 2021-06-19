from app import db
from flask import render_template, redirect, url_for, flash
from app.auth.authForm import LoginForm, RegisterForm
from app.usuarios.userModel import UserModel
from flask_login import login_user, current_user


class AuthController:
    def __init__(self):
        self.current_user = current_user

    def auth_login(self):
        if self.current_user.is_authenticated:
            return redirect(url_for('index'))

        form_login = LoginForm()
        if form_login.validate_on_submit():
            username = form_login.username.data
            password = form_login.password.data
            user = UserModel.query.filter_by(username=username).first()
            if user is None or not user.check_password(password):
                flash('Usuario y/o contraseña son incorrectos', 'danger')
                return redirect(url_for('login'))
            login_user(user)
            return redirect(url_for('index'))
        return render_template('views/auth/login.html', title='Inicia Sesion', form=form_login)

    def auth_register(self):
        form_register = RegisterForm()
        if form_register.validate_on_submit():
            username = form_register.username.data
            password = form_register.password.data
            address = form_register.address.data
            name = form_register.name.data
            document = form_register.document.data 

            user = UserModel.query.filter_by(username=username).first()
            if user:
                flash(f'El usuario {username} ya existe, pruebe con otro !', 'danger')
                return redirect(url_for('register'))
            
            user_add = UserModel(username=username, password=password,address=address,name=name,document=document,rol_id=2)
            user_add.hash_password()
            db.session.add(user_add)
            db.session.commit()

            flash(f'El usuario {username} se creo con exito !', 'light-primary')
            return redirect(url_for('login'))
        return render_template('views/auth/register.html', title='Registrate', form=form_register)