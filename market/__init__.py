from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


# Need the application
app = Flask(__name__)

# Need a security token to secure the app from CSRF Attacks
app.config['SECRET_KEY'] = "9037e7832479e476002a18ab"

# Need the database, manipulated with an ORM (SQLAlchemy in our case)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///market.db"
db = SQLAlchemy(app)

# Need a hash library to handle the information security
bcrypt = Bcrypt(app)

# To solve the runtime error of context application when using the sqlite db
app.app_context().push()

# Use a login manager
login_manager = LoginManager(app)

"""
What are these elements instanciated here ?
Like the database and all the rest. What do they form ?
How to organise them in a course ?
"""

# Need the routes handled by our application
from market import routes