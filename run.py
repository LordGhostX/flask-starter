from app import app, routes
from app.models import db

db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
