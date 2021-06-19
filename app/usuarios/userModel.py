from app import db, login

from flask_bcrypt import generate_password_hash, check_password_hash

from flask_login import UserMixin
class UserModel(UserMixin, db.Model): 
    
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    document = db.Column(db.Integer)
    address = db.Column(db.String(100))
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(150))
    rol_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    #se relacione con el nombre del modelo de la  tabla
    rol = db.relationship('RolesModel', back_populates='users')
    ventas = db.relationship('VentaModel', back_populates='users')
    
    def __repr__(self):
        return f'User: {self.username}'

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)


@login.user_loader
def load_user(user_id):
    return UserModel.query.get(int(user_id))