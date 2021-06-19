from app import db
from app.sub_categories.subcategoriesModel import SubCategoriesModel
from flask import flash, redirect, url_for


class SubCategoriesController():
    
    def records(self, page):
        return SubCategoriesModel.query.order_by(SubCategoriesModel.id).paginate(page=page, per_page=10)

    def create(self, form):
        try:
            name_category = form.name.data
            subcategory = SubCategoriesModel(name=name_category, status=1)
            db.session.add(subcategory)
            db.session.commit()
            flash(f'Se creo la categoria {name_category} con exito', category='light-primary color-primary')
            return redirect(url_for('subcategories'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error al crear la subcategoria --> {str(e)}', category='danger')
            return redirect(url_for('subcategories_create'))
        
        
    
    def update(self, form, subcategory_id):
        try:
            sub_name_category = form.name.data
            subcategory = SubCategoriesModel.query.filter_by(id=subcategory_id).first()
            subcategory.name = sub_name_category
            db.session.commit()
            flash(f'Se actilizó la subcategoria {sub_name_category} con exito', category='light-primary color-primary')
            return redirect(url_for('subcategories'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error en la actualización de la subcategoria --> {str(e)}', category='danger')
            return redirect(url_for('subcategories_update', id=subcategory_id))
        
        
        
    def delete(self, subcategory_id):
        try:
            subcategory = SubCategoriesModel.query.filter_by(id=subcategory_id).first()
            status = 0 if subcategory.status == 1 else 1
            subcategory.status = status
            db.session.commit()
            flash(f'Se cambió el estado con exito', category='light-primary color-primary')
            return redirect(url_for('subcategories'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error en la actualización de la subcategoria --> {str(e)}', category='danger')
            return redirect(url_for('subcategories'))
    