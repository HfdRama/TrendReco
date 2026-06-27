import os
from flask import Flask, render_template, session, flash, redirect, url_for
from extensions import db, cache # Import cache dari extensions
import models

# IMPORT ROUTE DARI FOLDER routes/
from routes.common import common_bp
from routes.user import init_user_routes
from routes.admin import init_admin_routes
from routes.chatbot import init_chatbot_routes
import pymysql


print("APP START")
app = Flask(__name__)
app.secret_key = "kunci_rahasia_skripsi_2026"

# --- KONFIGURASI DATABASE ---
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://root:@localhost/db_trendreco"
)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# --- KONFIGURASI CACHE (SimpleCache untuk RAM) ---
app.config['CACHE_TYPE'] = 'SimpleCache'
app.config['CACHE_DEFAULT_TIMEOUT'] = 3600 # Cache disimpan selama 1 jam (3600 detik)

# Inisialisasi DB dan Cache
db.init_app(app)
cache.init_app(app) 

# --- KONFIGURASI FOLDER UPLOAD ---
UPLOAD_FOLDER = 'uploads/datasets'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(os.path.join(UPLOAD_FOLDER, 'sosmed'), exist_ok=True)
os.makedirs(os.path.join(UPLOAD_FOLDER, 'gtrends'), exist_ok=True)

app.register_blueprint(common_bp)
# --- INISIALISASI ROUTE ---
init_user_routes(app)
init_admin_routes(app)
init_chatbot_routes(app)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
