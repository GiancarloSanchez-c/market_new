from app import db


class StockVenta(db.Model): 
    
    __tablename__ = 'stock_venta'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cod_producto = db.Column(db.Integer)
    nombre_venta = db.Column(db.String(100))
    cantidad_venta = db.Column(db.Integer)
    impuesto = db.Column(db.Integer)
    costo_venta = db.Column(db.Integer)
    descripcion = db.Column(db.String(100))
    almacen_id = db.Column(db.Integer, db.ForeignKey('almacen.id'))
    
    almacen = db.relationship('AlmacenModel',back_populates='stockventa')
    
    
    
    
    detail_venta = db.relationship('DetailVenta', back_populates='stock_venta')