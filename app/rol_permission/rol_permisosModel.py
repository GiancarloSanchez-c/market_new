from app import db 

class Rol_PermisosModel(db.Model):
    
    __tablename__ = 'permisos'
    
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(120),index=True)
    rol_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    
    rol = db.relationship('RolesModel', back_populates='rol_permission')
    
    def __repr__(self):
        return f'Rol: {self.name}'    