from flask import jsonify
from models.product import get_all_products

def product_routes(app, mysql):
    @app.route('/api/products')
    def products():
        return jsonify(products=get_all_products(mysql))
