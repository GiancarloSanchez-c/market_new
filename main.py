from app import app

from app.menu import menuModel
from app.roles import rolModel
from app.rol_permission import rol_permisosModel
from app.usuarios import userModel
from app.categories import categoriesModel
from app.sub_categories import subcategoriesModel
from app.detailCategories import detallesCategoriasModel
from app.almacen import almacenModel
from app.stockVenta import stockVenta
from app.venta import ventaModel
from app.detailVenta import detailVentaModel


from app.menu import menuRouter
from app.auth import authRouter
from app.home import homeRouter
from app.categories import categoriesRouter
from app.sub_categories import subcategoriesRouter