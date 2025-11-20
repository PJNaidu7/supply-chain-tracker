**📦 Supply Chain Tracker**

A lightweight, modular Supply Chain Tracking system built using Flask, MySQL, Bootstrap, Chart.js, and Machine Learning models (Random Forest + Isolation Forest).
This project supports product management, dashboard visualization, and AI-powered analytics for demand forecasting and bottleneck detection.

🚀 **Features**
🔹 Product Management

Add, update, delete, and list products

Organized through REST-style Flask routes (routes/products.py)

MySQL-backed storage defined in models/product.py

🔹 **Dashboard** (UI)

Built using Bootstrap 5 + Chart.js

Dynamic charts handled by static/js/dashboard.js

Template system (base.html, dashboard.html)

**🔹 Machine Learning
**
Located in /ml_models/:

Demand Forecasting (RandomForestRegressor)

Bottleneck Detection (IsolationForest)

These modules provide predictive analytics to enhance supply chain decision-making.

**🏗️ Project Structure
**supply_chain_project/
supply_chain_project/
│── app.py
│── config.py
│── requirements.txt
│── models/
│     └── product.py
│
│── routes/
│     ├── __init__.py
│     └── products.py
│
│── ml_models/
│     ├── __init__.py
│     ├── demand_forecasting.py
│     └── bottleneck_detection.py
│
│── templates/
│     ├── base.html
│     └── dashboard.html
│
│── static/
      ├── css/main.css
      └── js/dashboard.js

**⚙️ Installation & Setup
**1. Clone the repository
git clone https://github.com/your-username/supply-chain-tracker.git
cd supply-chain-tracker

2. Create a virtual environment
python -m venv venv
venv/Scripts/activate  # Windows

3. Install dependencies
pip install -r requirements.txt

4. Configure Database

Update config.py with your MySQL credentials:

MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "your_password"
MYSQL_DB = "supply_chain"
SECRET_KEY = "your_secret_key"

5. Create MySQL Database
CREATE DATABASE supply_chain;


(If you need table creation SQL, I can generate it from your models.)

**▶️ Run the Application
**python app.py


Visit:

http://127.0.0.1:5000/

**🧠 Machine Learning Modules
**🔹 Demand Forecasting (ml_models/demand_forecasting.py)

Uses Random Forest to predict future product demand

Works on time-series and historical order features

🔹 Bottleneck Detection (ml_models/bottleneck_detection.py)

Uses Isolation Forest to flag anomalies

Useful for detecting delays, irregular processing times, or unusual vendor performance

**📊 Dashboard
**
Real-time data visualizations

Charts powered by Chart.js

Layout defined in dashboard.html

JS logic handled in static/js/dashboard.js

**🛠️ Future Enhancements
**
Multi-role authentication (Admin, Manager, QC, Staff)

Vendor management module

Inventory management

Complete workflow tracking (batch → qc → warehouse → delivery)

LSTM-based advanced forecasting

🤝 Contributing

Pull requests are welcome.
For major changes, please open an issue first to discuss what you’d like to modify.
