import os
import pymysql
pymysql.install_as_MySQLdb()

from flask import Flask
from extensions import db, cache
import models

# Routes
from routes.common import common_bp
from routes.user import init_user_routes
from routes.admin import init_admin_routes
from routes.chatbot import init_chatbot_routes

print("APP START")

app = Flask(__name__)
app.secret_key = "kunci_rahasia_skripsi_2026"

# =========================
# HEALTH CHECK ROUTE (WAJIB)
# =========================
@app.route("/")
def home():
    return "TrendReco is running"

@app.route("/ping")
def ping():
    return "ok"


# =========================
# DATABASE CONFIG
# =========================
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://root:@localhost/db_trendreco"
)

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# =========================
# CACHE CONFIG
# =========================
app.config["CACHE_TYPE"] = "SimpleCache"
app.config["CACHE_DEFAULT_TIMEOUT"] = 3600


# =========================
# INIT EXTENSIONS
# =========================
db.init_app(app)
cache.init_app(app)


# =========================
# UPLOAD FOLDER
# =========================
UPLOAD_FOLDER = "uploads/datasets"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(os.path.join(UPLOAD_FOLDER, "sosmed"), exist_ok=True)
os.makedirs(os.path.join(UPLOAD_FOLDER, "gtrends"), exist_ok=True)


# =========================
# REGISTER BLUEPRINTS
# =========================
app.register_blueprint(common_bp)

init_user_routes(app)
init_admin_routes(app)
init_chatbot_routes(app)


# =========================
# CREATE TABLES (DEV ONLY)
# =========================
if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)