from werkzeug.security import generate_password_hash

from app.extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email
        }

    def set_password(self, password):
        self.password = generate_password_hash(password)
