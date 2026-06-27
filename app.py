import os
import pymysql
pymysql.install_as_MySQLdb()

from flask import Flask
from extensions import db, cache

# IMPORT ROUTES
from routes.common import common_bp
from routes.user import init_user_routes
from routes.admin import init_admin_routes
from routes.chatbot import init_chatbot_routes

print("APP START")

app = Flask(__name__)
app.secret_key = "kunci_rahasia_skripsi_2026"

# ======================
# CONFIG DATABASE
# ======================
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://root:@localhost/db_trendreco"
)

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# ======================
# CACHE
# ======================
app.config["CACHE_TYPE"] = "SimpleCache"
app.config["CACHE_DEFAULT_TIMEOUT"] = 3600

# ======================
# INIT EXTENSIONS
# ======================
db.init_app(app)
cache.init_app(app)

# ======================
# IMPORT MODELS (PENTING)
# ======================
with app.app_context():
    import models
    db.create_all()

# ======================
# UPLOAD FOLDER
# ======================
UPLOAD_FOLDER = "uploads/datasets"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(os.path.join(UPLOAD_FOLDER, "sosmed"), exist_ok=True)
os.makedirs(os.path.join(UPLOAD_FOLDER, "gtrends"), exist_ok=True)

# ======================
# ROUTES
# ======================
@app.route("/")
def home():
    return "index.html"

app.register_blueprint(common_bp)
init_user_routes(app)
init_admin_routes(app)
init_chatbot_routes(app)

# ======================
# RUN APP
# ======================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)