from app import db

class Photo(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    title: str = db.Column(db.String(100), nullable=False)
    description: str = db.Column(db.Text, nullable=True)
    image: str = db.Column(db.String, nullable=False)

    def __repr__(self) -> str:
        return f'<Photo {self.title}>'
