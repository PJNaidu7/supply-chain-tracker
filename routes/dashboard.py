from flask import render_template, jsonify

def dashboard_routes(app, mysql):
    @app.route('/')
    def dashboard():
        return render_template('dashboard.html')

    @app.route('/api/supply-chain-status')
    def supply_chain_status():
        cur = mysql.connection.cursor()
        cur.execute("SELECT COUNT(*) FROM products")
        total_products = cur.fetchone()[0]

        cur.execute("SELECT SUM(price * stock) FROM products")
        inventory_value = cur.fetchone()[0] or 0

        cur.close()
        return jsonify({
            "status": "Operational",
            "total_products": total_products,
            "inventory_value": inventory_value
        })

    @app.route('/api/bottleneck-alerts')
    def bottleneck_alerts():
        cur = mysql.connection.cursor()
        cur.execute("SELECT name, stock FROM products WHERE stock < 10")
        low_stock = cur.fetchall()
        cur.close()
        alerts = [f"Low stock: {name} ({stock})" for name, stock in low_stock]
        return jsonify({"bottlenecks": alerts})
