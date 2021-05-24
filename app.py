from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import sql

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@34.89.53.54:3306/car_detailing"

db = SQLAlchemy(app)





if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
