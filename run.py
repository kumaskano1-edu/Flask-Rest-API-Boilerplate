from flask import Flask
from model import db
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    
    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    db.init_app(app)
    return app


if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)