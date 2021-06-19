from app import app
from flask import render_template, request
from flask_login import login_required
from app.sub_categories.subcategoriesController import SubCategoriesController
from app.sub_categories.subcategoriesForm import SubCategoriesForm
from app.sub_categories.subcategoriesModel import SubCategoriesModel

@app.route('/subcategories')
@login_required
def subcategories():
    page = request.args.get('page', type=int, default=1)
    controller = SubCategoriesController()
    subcategories = controller.records(page)
    return render_template('views/subCategories/index.html', title='SubCategorias', data=subcategories)


@app.route('/subcategories/create', methods=['GET', 'POST'])
@login_required
def subcategories_create():
    form = SubCategoriesForm()
    if form.validate_on_submit():
        controller = SubCategoriesController()
        return controller.create(form)
    return render_template('views/subCategories/forms/create.html', title='Crear Subcategorias', form=form)

@app.route('/subcategories/update/<int:id>', methods=['GET', 'POST'])
@login_required
def subcategories_update(id):
    subcategory = SubCategoriesModel.query.get_or_404(id)
    form = SubCategoriesForm(obj=subcategory)
    if form.validate_on_submit():
        controller = SubCategoriesController()
        return controller.update(form, id)
    return render_template('views/subCategories/forms/update.html', title='Actualizar Subcategorias', form=form, subcategory_id=subcategory.id)

@app.route('/subcategories/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def subcategories_delete(id):
    controller = SubCategoriesController()
    return controller.delete(id)
    
