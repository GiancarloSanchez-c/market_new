from app import db

class SubCategoriesModel(db.Model):
    
    __tablename__ = 'sub_categories'
    
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(120),index=True)
    status = db.Column(db.Integer)
    categories_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    
    ###
    
    categories = db.relationship('CategoriesModel', back_populates='sub_categories')
    
    detail_categories = db.relationship('DetailCategories',back_populates='sub_categories')
    
    
    
    
    def __repr__(self):
        return f'Sub_Categoria: {self.name}'