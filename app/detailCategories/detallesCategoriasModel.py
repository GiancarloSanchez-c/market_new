from app import db

class DetailCategories(db.Model):
    
    __tablename__ = 'detail_categories'
    
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(120),index=True) 
    sub_categories_id = db.Column(db.Integer, db.ForeignKey('sub_categories.id'))
    
    ###
    
    sub_categories= db.relationship('SubCategoriesModel', back_populates='detail_categories')
    
    almancen = db.relationship('AlmacenModel', back_populates='detail_categories')
    
    def __repr__(self):
        return f'Name: {self.name}'