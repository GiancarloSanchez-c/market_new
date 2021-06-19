from app import db


class DetailVenta(db.Model): 
    
    __tablename__ = 'detalle_venta'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    venta_id = db.Column(db.Integer, db.ForeignKey('venta.id'))
    stock_venta_id = db.Column(db.Integer, db.ForeignKey('stock_venta.id'))
    cantidad = db.Column(db.Integer)
    costo_unitario = db.Column(db.Integer)
    importe = db.Column(db.Integer)
    
    
    venta = db.relationship('VentaModel', back_populates='detail_venta')
    stock_venta = db.relationship('StockVenta', back_populates='detail_venta')