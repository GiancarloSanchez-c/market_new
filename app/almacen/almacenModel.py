from app import db

class AlmacenModel(db.Model): 
    
    __tablename__ = 'almacen'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    marca = db.Column(db.String(100))
    cantidad_paquetes = db.Column(db.Integer)
    cantidad_unidades = db.Column(db.Integer)
    presentacion = db.Column(db.String(150))
    fecha_ingreso = db.Column(db.DateTime)
    datail_categories_id = db.Column(db.Integer, db.ForeignKey('detail_categories.id'))

    
    stockventa = db.relationship('StockVenta',back_populates='almacen')
    
    
    detail_categories = db.relationship('DetailCategories',back_populates='almancen')