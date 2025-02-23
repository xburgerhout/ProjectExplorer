from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap

from app.errors import bp as errors_bp

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(errors_bp)

bootstrap = Bootstrap(app)

from app import routes
