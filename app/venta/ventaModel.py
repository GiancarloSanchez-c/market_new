from app import db


class VentaModel(db.Model): 
    
    __tablename__ = 'venta'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    serie = db.Column(db.Integer)
    sub_total = db.Column(db.Integer)
    total_impuesto = db.Column(db.Integer)
    total = db.Column(db.Integer)
    fecha_venta = db.Column(db.DateTime)
    estado_venta = db.Column(db.String(50))
    usuario_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    users = db.relationship('UserModel', back_populates='ventas')
    
    detail_venta = db.relationship('DetailVenta', back_populates='venta')