from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

from models import db
from routes.auth_routes import auth_bp
from routes.task_routes import task_bp

load_dotenv()

app = Flask(__name__)
# Enable CORS for the frontend port
CORS(app, resources={r"/api/*": {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'mysql+pymysql://root:root@localhost:3306/taskmanager')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(task_bp, url_prefix='/api/tasks')

if __name__ == '__main__':
    with app.app_context():
        # This will create tables on startup if they don't exist
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)


with app.app_context():
    db.create_all()