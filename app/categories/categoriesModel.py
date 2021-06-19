from app import db

class CategoriesModel(db.Model):
    
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(120),index=True) 
    
    
    sub_categories = db.relationship('SubCategoriesModel', back_populates='categories')
    
    
    
    
    def __repr__(self):
        return f'Categoria: {self.name}'