from app import db
from app.categories.categoriesModel import CategoriesModel
from flask import flash, redirect, url_for


class CategoriesController():
    
    def records(self, page):
        return CategoriesModel.query.order_by(CategoriesModel.id).paginate(page=page, per_page=10)

    def create(self, form):
        try:
            name_category = form.name.data
            category = CategoriesModel(name=name_category , status=1)
            db.session.add(category)
            db.session.commit()
            flash(f'Se creo la categoria {name_category} con exito', category='light-primary color-primary')
            return redirect(url_for('categories'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error al crear la categoria --> {str(e)}', category='danger')
            return redirect(url_for('categories_create'))
        
        
    
    def update(self, form, category_id):
        try:
            name_category = form.name.data
            category = CategoriesModel.query.filter_by(id=category_id).first()
            category.name = name_category
            db.session.commit()
            flash(f'Se actilizó la categoria {name_category} con exito', category='light-primary color-primary')
            return redirect(url_for('categories'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error en la actualización de la categoria --> {str(e)}', category='danger')
            return redirect(url_for('categories_update', id=category_id))
        
        
        
    def delete(self, category_id):
        try:
            category = CategoriesModel.query.filter_by(id=category_id).first()
            status = 0 if category.status == 1 else 1
            category.status = status
            db.session.commit()
            flash(f'Se cambió el estado con exito', category='light-primary color-primary')
            return redirect(url_for('categories'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error en la actualización de la categoria --> {str(e)}', category='danger')
            return redirect(url_for('categories_update', id=category_id))
    