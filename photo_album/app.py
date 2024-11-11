from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


class PhotoAlbum(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    image_path = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<PhotoAlbum {self.id} - {self.description}>'


with app.app_context():
    db.create_all()  

from routes import *

if __name__ == "__main__":
    app.run(debug=True)
